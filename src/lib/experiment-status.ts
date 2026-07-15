import type { CollectionEntry } from 'astro:content';

export type ExperimentStatus =
  | 'Planned'
  | 'Running'
  | 'Completed'
  | 'Rejected'
  | 'Archived';

export type EvidenceLevel = 'A' | 'B' | 'C' | 'D';

export type ExperimentData = CollectionEntry<'experiments'>['data'];

export const evidenceLevelMeaning: Record<EvidenceLevel, string> = {
  A: 'Confirmed with data and repeated',
  B: 'Confirmed once',
  C: 'Initial observation underway',
  D: 'Hypothesis only (no observation archive yet)',
};

export const statusMeaning: Record<ExperimentStatus, string> = {
  Planned: 'Protocol defined; measurement not started',
  Running: 'Intervention and/or data collection in progress',
  Completed: 'Measurement finished; results from archived captures',
  Rejected: 'Stopped; hypothesis not pursued or protocol abandoned',
  Archived: 'Closed historically; kept for reference',
};

/** Calendar day in UTC (YYYY-MM-DD), for stable schedule comparisons. */
export function toUtcDay(date: Date): string {
  return date.toISOString().slice(0, 10);
}

/**
 * Resolve display status from manual frontmatter + optional startsOn.
 *
 * Terminal states (Completed, Rejected, Archived) never auto-change.
 * Running stays Running.
 * Planned + startsOn ≤ today → Running.
 */
export function resolveEffectiveStatus(
  data: Pick<ExperimentData, 'status' | 'startsOn'>,
  now: Date = new Date(),
): ExperimentStatus {
  if (
    data.status === 'Completed' ||
    data.status === 'Rejected' ||
    data.status === 'Archived' ||
    data.status === 'Running'
  ) {
    return data.status;
  }

  if (data.status === 'Planned' && data.startsOn) {
    if (toUtcDay(now) >= toUtcDay(data.startsOn)) {
      return 'Running';
    }
  }

  return data.status;
}

export function activationLabel(
  data: Pick<ExperimentData, 'status' | 'startsOn'>,
  now: Date = new Date(),
): string | null {
  if (
    data.status === 'Completed' ||
    data.status === 'Rejected' ||
    data.status === 'Archived'
  ) {
    return null;
  }
  if (!data.startsOn) return null;

  const start = toUtcDay(data.startsOn);
  const today = toUtcDay(now);

  if (data.status === 'Planned' && today < start) {
    return `Activates ${start}`;
  }

  if (resolveEffectiveStatus(data, now) === 'Running') {
    return `Started ${start}`;
  }

  return null;
}
