# Changelog

Versions follow [Semantic Versioning](https://semver.org/) (`<major>.<minor>.<patch>`).

Backward incompatible (breaking) changes will only be introduced in major versions
with advance notice in the **Deprecations** section of releases.

<!--
You should *NOT* be adding new changelog entries to this file,
this file is managed by towncrier.
See `changelog/README.md`.

To update this file, run

```
towncrier build --version <desired-version-string>
```

We may one day automate this in a GitHub action,
for now, just run it by hand.
You will need a virtual environment with towncrier installed to do so
(e.g. `python3 -m venv venv; source venv/bin/activate; pip install towncrier`).

You *may* edit previous changelogs to fix problems like typo corrections or such.
To add a new changelog entry, please see
`changelog/README.md`
and https://pip.pypa.io/en/latest/development/contributing/#news-entries,
noting that we use the `changelog` directory instead of news,
markdown instead of restructured text and use slightly different categories
from the examples given in that link.
-->

<!-- towncrier release notes start -->

## Variable registry v0.1.0 (2025-09-10)

### ⚠️ Breaking Changes

- Updated all variable entries (`src-data/variable`) to match v1.2.2 of the data request ([#42](https://github.com/WCRP-CMIP/Variable-Registry/pull/42))
