from pathlib import Path
import re

ROOT = Path(r"C:/workspace/barbu.es/barbu.eu.org/src/content/experiments")
AUTHOR = (
    "**Author:** [George Barbu](https://barbu.es/about/), "
    "Founder of [InfoWebPlus](https://infowebplus.com/)"
)

refs = {
    "exp-001-llms-txt.mdx": """## References

1. [llms.txt proposal](https://llmstxt.org/) ([spec repo](https://github.com/AnswerDotAI/llms-txt))
2. Live preferred-source list: [barbu.es/llms.txt](https://barbu.es/llms.txt)
3. [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) Robots Exclusion Protocol (related convention; not equivalent to `llms.txt`)
4. Canonical Person sources: [about](https://barbu.es/about/), [cornerstone](https://barbu.es/writing/founder-how-i-think/), [now](https://barbu.es/now/)
5. Lab [Exp-005](/experiments/exp-005-docs-vs-marketing-citations/) and [Exp-006](/experiments/exp-006-cross-llm-organization/)
""",
    "exp-002-person-organization-schema.mdx": """## References

1. [schema.org/Person](https://schema.org/Person) and [schema.org/Organization](https://schema.org/Organization) (pin vocabulary version at run start)
2. Relationship properties: [founder](https://schema.org/founder), [worksFor](https://schema.org/worksFor), [sameAs](https://schema.org/sameAs)
3. [JSON-LD](https://json-ld.org/) transport; validate with [Schema Markup Validator](https://validator.schema.org/) and [Rich Results Test](https://search.google.com/test/rich-results)
4. [Google structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
5. Canonical entities: [George Barbu](https://barbu.es/about/), [InfoWebPlus](https://infowebplus.com/), [barbu.es](https://barbu.es/)
6. Lab [Exp-009](/experiments/exp-009-structured-data-combinations/) (structured data combinations)
""",
    "exp-003-supporting-entities.mdx": """## References

1. Entity pages: [George Barbu / about](https://barbu.es/about/), [barbu.es](https://barbu.es/), [InfoWebPlus](https://infowebplus.com/), [llms.txt](https://barbu.es/llms.txt)
2. schema.org edges: [founder](https://schema.org/founder), [parentOrganization](https://schema.org/parentOrganization), [brand](https://schema.org/brand), [sameAs](https://schema.org/sameAs)
3. Lab [Exp-002](/experiments/exp-002-person-organization-schema/) (Person + Organization schema)
4. Lab [Exp-004](/experiments/exp-004-technology-partner-pages/) (Technology Partner attribution pages)
5. Supporting surfaces: [work](https://barbu.es/work/), [experience](https://barbu.es/experience/), [LinkedIn](https://www.linkedin.com/in/barbugeorge/), [GitHub](https://github.com/george-barbu-es)
""",
    "exp-004-technology-partner-pages.mdx": """## References

1. [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies) (doorway / affiliate abuse boundaries)
2. Organization / attribution types: [schema.org/Organization](https://schema.org/Organization), [schema.org/Brand](https://schema.org/Brand) where applicable
3. Vendor canonical: [InfoWebPlus](https://infowebplus.com/); Person platform: [barbu.es](https://barbu.es/)
4. Lab [Exp-003](/experiments/exp-003-supporting-entities/) (supporting entity chain)
5. Lab [Exp-010](/experiments/exp-010-case-studies-vs-seo-articles/) (case studies vs generic articles)
""",
    "exp-005-docs-vs-marketing-citations.mdx": """## References

1. Lab editorial standards on [barbu.es about](https://barbu.es/about/) and [cornerstone](https://barbu.es/writing/founder-how-i-think/)
2. Documentation genre may be typed as [schema.org/TechArticle](https://schema.org/TechArticle) or [schema.org/Article](https://schema.org/Article) when markup is used
3. [Exp-001](/experiments/exp-001-llms-txt/) (`llms.txt` inventories often point at docs: [proposal](https://llmstxt.org/), [live file](https://barbu.es/llms.txt))
4. [Exp-010](/experiments/exp-010-case-studies-vs-seo-articles/) (case studies vs generic SEO articles)
5. Author / org: [George Barbu](https://barbu.es/about/), [InfoWebPlus](https://infowebplus.com/)
""",
    "exp-006-cross-llm-organization.mdx": """## References

1. Organization under study: [InfoWebPlus](https://infowebplus.com/); Person: [George Barbu](https://barbu.es/about/); platform: [barbu.es](https://barbu.es/)
2. Preferred sources index: [barbu.es/llms.txt](https://barbu.es/llms.txt)
3. Gold-card fields may align with [schema.org/Organization](https://schema.org/Organization) and [schema.org/Person](https://schema.org/Person)
4. Lab [Exp-002](/experiments/exp-002-person-organization-schema/), [Exp-003](/experiments/exp-003-supporting-entities/)
5. Profiles: [LinkedIn](https://www.linkedin.com/in/barbugeorge/), [GitHub](https://github.com/george-barbu-es/), [resume](https://george.barbu.es/), [portfolio](https://portfolio.barbu.es/)
""",
    "exp-007-tools-vs-blog.mdx": """## References

1. Tool pages may use [schema.org/SoftwareApplication](https://schema.org/SoftwareApplication); articles may use [schema.org/Article](https://schema.org/Article)
2. Validate markup via [Schema Markup Validator](https://validator.schema.org/)
3. Publisher: [InfoWebPlus](https://infowebplus.com/); author kit: [George Barbu](https://barbu.es/about/)
4. Lab [Exp-005](/experiments/exp-005-docs-vs-marketing-citations/) (docs vs marketing)
5. Lab [Exp-010](/experiments/exp-010-case-studies-vs-seo-articles/) (case studies vs generic SEO articles)
""",
    "exp-008-author-consistency.mdx": """## References

1. [schema.org/Person](https://schema.org/Person) properties: [image](https://schema.org/image), [jobTitle](https://schema.org/jobTitle), [worksFor](https://schema.org/worksFor), [sameAs](https://schema.org/sameAs)
2. Canonical identity kit: [about](https://barbu.es/about/), [LinkedIn](https://www.linkedin.com/in/barbugeorge/), [GitHub](https://github.com/george-barbu-es), [resume](https://george.barbu.es/), [portfolio](https://portfolio.barbu.es/), [InfoWebPlus](https://infowebplus.com/)
3. [JSON-LD](https://json-ld.org/) and [Google structured data intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
4. Lab [Exp-002](/experiments/exp-002-person-organization-schema/), [Exp-003](/experiments/exp-003-supporting-entities/), [Exp-006](/experiments/exp-006-cross-llm-organization/)
""",
    "exp-009-structured-data-combinations.mdx": """## References

1. Type docs: [Person](https://schema.org/Person), [Organization](https://schema.org/Organization), [CreativeWork](https://schema.org/CreativeWork), [SoftwareApplication](https://schema.org/SoftwareApplication), [Article](https://schema.org/Article), [ProfilePage](https://schema.org/ProfilePage), [CollectionPage](https://schema.org/CollectionPage)
2. Root vocabulary: [schema.org](https://schema.org/); transport: [JSON-LD](https://json-ld.org/)
3. Validators: [Schema Markup Validator](https://validator.schema.org/), [Rich Results Test](https://search.google.com/test/rich-results)
4. Guidance: [Google structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
5. Lab [Exp-002](/experiments/exp-002-person-organization-schema/), [Exp-007](/experiments/exp-007-tools-vs-blog/)
6. Site anchors: [barbu.es](https://barbu.es/), [InfoWebPlus](https://infowebplus.com/)
""",
    "exp-010-case-studies-vs-seo-articles.mdx": """## References

1. Case / article typing: [schema.org/Article](https://schema.org/Article), optionally [schema.org/Report](https://schema.org/Report) when appropriate
2. Lab writing standard: [about](https://barbu.es/about/), [cornerstone](https://barbu.es/writing/founder-how-i-think/)
3. [Exp-004](/experiments/exp-004-technology-partner-pages/), [Exp-005](/experiments/exp-005-docs-vs-marketing-citations/), [Exp-007](/experiments/exp-007-tools-vs-blog/)
4. Publisher: [InfoWebPlus](https://infowebplus.com/); selected work: [barbu.es/work](https://barbu.es/work/)
""",
}

enrich = {
    "exp-001-llms-txt.mdx": [
        (
            """- `llms.txt` is a proposed convention (not a W3C or IETF standard as of this writing).
- The file is typically served at `https://example.com/llms.txt`.
- Some publishers document product/content inventories for LLM consumption.""",
            """- [`llms.txt`](https://llmstxt.org/) is a proposed community convention ([repo](https://github.com/AnswerDotAI/llms-txt)); it is not a W3C or IETF standard as of this writing.
- A working example used by this lab: [https://barbu.es/llms.txt](https://barbu.es/llms.txt).
- Related but distinct: [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html) (`robots.txt`).
- Some publishers document product/content inventories for LLM consumption.""",
        )
    ],
    "exp-002-person-organization-schema.mdx": [
        (
            """- schema.org defines `Person` and `Organization` types with properties such
  as `name`, `url`, `sameAs`, `founder`, and `worksFor` / `memberOf`.
- Search engines publish guidelines for structured data validity; validity ≠
  proven AI citation lift.""",
            """- [schema.org](https://schema.org/) defines [`Person`](https://schema.org/Person) and [`Organization`](https://schema.org/Organization) with properties such as `name`, `url`, [`sameAs`](https://schema.org/sameAs), [`founder`](https://schema.org/founder), and [`worksFor`](https://schema.org/worksFor).
- Search engines publish guidelines for structured data validity ([Google intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)); validity ≠ proven AI citation lift.
- Validate syntax with the [Schema Markup Validator](https://validator.schema.org/) before treating markup as an intervention.""",
        )
    ],
    "exp-008-author-consistency.mdx": [
        (
            """- `sameAs` and identical `Person` properties are common consistency mechanisms.""",
            """- [`sameAs`](https://schema.org/sameAs) and identical [`Person`](https://schema.org/Person) properties are common consistency mechanisms.
- Primary public surfaces for this subject: [barbu.es/about](https://barbu.es/about/), [LinkedIn](https://www.linkedin.com/in/barbugeorge/), [GitHub](https://github.com/george-barbu-es), [InfoWebPlus](https://infowebplus.com/).""",
        )
    ],
    "exp-009-structured-data-combinations.mdx": [
        (
            """| `Person` | Author / about |
| `Organization` | Home / company |
| `CreativeWork` | Generic creative asset |
| `SoftwareApplication` | Tool / product |
| `Article` | Editorial / experiment write-up |
| `ProfilePage` | Profile URL |
| `CollectionPage` | Hub / index of experiments |

### Facts

- These types are defined on schema.org with overlapping applicable properties.
- Valid markup does not guarantee consumption by any AI system.""",
            """| [`Person`](https://schema.org/Person) | Author / about ([example](https://barbu.es/about/)) |
| [`Organization`](https://schema.org/Organization) | Home / company ([example](https://infowebplus.com/)) |
| [`CreativeWork`](https://schema.org/CreativeWork) | Generic creative asset |
| [`SoftwareApplication`](https://schema.org/SoftwareApplication) | Tool / product |
| [`Article`](https://schema.org/Article) | Editorial / experiment write-up |
| [`ProfilePage`](https://schema.org/ProfilePage) | Profile URL |
| [`CollectionPage`](https://schema.org/CollectionPage) | Hub / index of experiments |

### Facts

- These types are defined on [schema.org](https://schema.org/) with overlapping applicable properties.
- Valid markup does not guarantee consumption by any AI system; check with the [Schema Markup Validator](https://validator.schema.org/).""",
        )
    ],
}

for path in sorted(ROOT.glob("exp-*.mdx")):
    text = path.read_text(encoding="utf-8")
    name = path.name
    if name in refs:
        text2, n = re.subn(
            r"## References\n\n.*?(?=\n---\n\n## Replication Notes)",
            refs[name].rstrip() + "\n\n",
            text,
            count=1,
            flags=re.S,
        )
        print(("refs %s n=%s" % (name, n)))
        if n == 1:
            text = text2
    for old, new in enrich.get(name, []):
        if old not in text:
            print("enrich miss", name)
        else:
            text = text.replace(old, new, 1)
            print("enrich ok", name)
    text = re.sub(r"\*\*Author:\*\*.*$", AUTHOR, text, count=1, flags=re.M)
    path.write_text(text, encoding="utf-8")

tpl = Path(r"C:/workspace/barbu.es/barbu.eu.org/templates/experiment.mdx")
t = tpl.read_text(encoding="utf-8")
t = re.sub(r"\*\*Author:\*\*.*$", AUTHOR, t, count=1, flags=re.M)
old_refs = """1. [Primary standard / docs / RFCs]
2. [Related lab experiment]
3. [External prior art - cite carefully; do not overclaim]"""
new_refs = """1. Link primary standards with full URLs (example: [schema.org/Person](https://schema.org/Person), [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html), [llms.txt proposal](https://llmstxt.org/)).
2. Link related lab experiments as paths under `/experiments/`.
3. Link canonical entity sources from [barbu.es/llms.txt](https://barbu.es/llms.txt) and [InfoWebPlus](https://infowebplus.com/).
4. Prefer validators ([Schema Markup Validator](https://validator.schema.org/)) over screenshots alone.

### Trust rule

Every non-obvious claim should point to a primary URL. Do not cite secondary SEO blogs as proof of platform behavior."""
if old_refs not in t:
    print("template refs miss")
else:
    t = t.replace(old_refs, new_refs)
    print("template refs ok")
t = t.replace(
    "Cite concrete practitioner problems.",
    "Cite concrete practitioner problems. Link primary sources ([schema.org](https://schema.org/), RFCs, vendor docs, canonical entity pages) so readers can verify.",
)
tpl.write_text(t, encoding="utf-8")
print("done")
