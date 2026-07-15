/**
 * Client-side schedule resolution so Planned → Running flips on startsOn
 * without requiring a redeploy. Terminal statuses never auto-change.
 */
(function () {
  var TERMINAL = { Completed: 1, Rejected: 1, Archived: 1, Running: 1 };

  function utcDay(d) {
    return d.toISOString().slice(0, 10);
  }

  function resolve(manual, startsOn, now) {
    if (TERMINAL[manual]) return manual;
    if (manual === 'Planned' && startsOn && utcDay(now) >= startsOn) {
      return 'Running';
    }
    return manual;
  }

  function apply() {
    var now = new Date();
    document.querySelectorAll('[data-status-manual]').forEach(function (el) {
      var manual = el.getAttribute('data-status-manual') || 'Planned';
      var startsOn = el.getAttribute('data-starts-on');
      var effective = resolve(manual, startsOn, now);
      var label = el.getAttribute('data-status-label');
      el.textContent = label ? label.replace('{status}', effective) : effective;
      el.className = el.className
        .replace(/\bstatus-(planned|running|completed|rejected|archived)\b/gi, '')
        .trim();
      el.classList.add('status', 'status-' + effective.toLowerCase());

      var scheduleEl =
        el.parentElement && el.parentElement.querySelector('[data-schedule-hint]');
      if (scheduleEl) {
        if (TERMINAL[manual] || !startsOn) {
          scheduleEl.hidden = true;
        } else if (manual === 'Planned' && utcDay(now) < startsOn) {
          scheduleEl.hidden = false;
          scheduleEl.textContent = 'Activates ' + startsOn;
        } else if (effective === 'Running') {
          scheduleEl.hidden = false;
          scheduleEl.textContent = 'Started ' + startsOn;
        } else {
          scheduleEl.hidden = true;
        }
      }
    });

    document.querySelectorAll('[data-live-count]').forEach(function (el) {
      var key = el.getAttribute('data-status-count');
      if (!key) return;
      el.textContent = String(
        document.querySelectorAll(
          '[data-status-manual].status-' + String(key).toLowerCase(),
        ).length,
      );
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
})();
