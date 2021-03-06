# Changelog

[PyPI History][1]

[1]: https://pypi.org/project/google-cloud-datastore/#history

## 1.8.0

05-17-2019 08:28 PDT

### Implementation Changes
- Add routing header to method metadata (via synth). ([#7593](https://github.com/googleapis/google-cloud-python/pull/7593))
- Remove classifier for Python 3.4 for end-of-life. ([#7535](https://github.com/googleapis/google-cloud-python/pull/7535))

### New Features
- Add `client_info` support to client. ([#8013](https://github.com/googleapis/google-cloud-python/pull/8013))

### Dependencies
- Pin `google-cloud-core >= 1.0.0, < 2.0dev`. ([#7993](https://github.com/googleapis/google-cloud-python/pull/7993))

### Documentation
- Update client library documentation URLs. ([#7307](https://github.com/googleapis/google-cloud-python/pull/7307))
- Pick up stub docstring fix in GAPIC generator. ([#6968](https://github.com/googleapis/google-cloud-python/pull/6968))

### Internal / Testing Changes
- Add nox session `docs` (via synth). ([#7768](https://github.com/googleapis/google-cloud-python/pull/7768))
- Copy lintified proto files (via synth). ([#7446](https://github.com/googleapis/google-cloud-python/pull/7446))
- Add clarifying comment to blacken nox target. ([#7389](https://github.com/googleapis/google-cloud-python/pull/7389))
- Add protos as an artifact to library ([#7205](https://github.com/googleapis/google-cloud-python/pull/7205))
- Update copyright headers ([#7142](https://github.com/googleapis/google-cloud-python/pull/7142))
- Protoc-generated serialization update. ([#7080](https://github.com/googleapis/google-cloud-python/pull/7080))

## 1.7.3

12-17-2018 16:45 PST


### Documentation
- Show use of 'batch.begin()' in docstring example. ([#6932](https://github.com/googleapis/google-cloud-python/pull/6932))
- Document Python 2 deprecation ([#6910](https://github.com/googleapis/google-cloud-python/pull/6910))

## 1.7.2

12-10-2018 12:37 PST


### Implementation Changes
- Fix client_info bug, update docstrings. ([#6409](https://github.com/googleapis/google-cloud-python/pull/6409))
- Pick up fixes in GAPIC generator. ([#6494](https://github.com/googleapis/google-cloud-python/pull/6494))
- Import `iam.policy` from `google.api_core`. ([#6741](https://github.com/googleapis/google-cloud-python/pull/6741))
- Pick up enum fixes in the GAPIC generator. ([#6610](https://github.com/googleapis/google-cloud-python/pull/6610))

### Dependencies
- Bump minimum `api_core` version for all GAPIC libs to 1.4.1. ([#6391](https://github.com/googleapis/google-cloud-python/pull/6391))
- Update version of google-cloud-core ([#6858](https://github.com/googleapis/google-cloud-python/pull/6858))

### Internal / Testing Changes
- Update noxfile.
- Add synth metadata. ([#6564](https://github.com/googleapis/google-cloud-python/pull/6564))
- blacken all gen'd libs ([#6792](https://github.com/googleapis/google-cloud-python/pull/6792))
- omit local deps ([#6701](https://github.com/googleapis/google-cloud-python/pull/6701))
- Run black at end of synth.py ([#6698](https://github.com/googleapis/google-cloud-python/pull/6698))
- Run Black on Generated libraries ([#6666](https://github.com/googleapis/google-cloud-python/pull/6666))
- Add templates for flake8, coveragerc, noxfile, and black. ([#6642](https://github.com/googleapis/google-cloud-python/pull/6642))

## 1.7.1

10-29-2018 10:38 PDT

### Implementation Changes
- Propagate empty arrays in entity values. ([#6285](https://github.com/googleapis/google-cloud-python/pull/6285))
- Expose 'Client.base_url' property to allow alternate endpoints. ([#5821](https://github.com/googleapis/google-cloud-python/pull/5821))

### Documentation
- Normalize use of support level badges ([#6159](https://github.com/googleapis/google-cloud-python/pull/6159))
- Redirect renamed 'usage.html'/'client.html' -> 'index.html'. ([#5996](https://github.com/googleapis/google-cloud-python/pull/5996))
- Replace links to '/stable/' with '/latest/'. ([#5901](https://github.com/googleapis/google-cloud-python/pull/5901))

### Internal / Testing Changes
- Use new Nox ([#6175](https://github.com/googleapis/google-cloud-python/pull/6175))
- Add 'synth.py'. ([#6078](https://github.com/googleapis/google-cloud-python/pull/6078))
- Prep datastore docs for repo split. ([#5919](https://github.com/googleapis/google-cloud-python/pull/5919))
- Use inplace installs under `nox` ([#5865](https://github.com/googleapis/google-cloud-python/pull/5865))

## 1.7.0

### Implementation Changes

- Do not pass 'offset' once the query iterator has a cursor (#5503)
- Add test runs for Python 3.7 and remove run for 3.4 (#5295)

### Documentation

- minor fix to datastore example (#5452)
- Add example showing explicit unicode for text values in entities. (#5263)

### Internal / Testing Changes

- Modify system tests to use prerelease versions of grpcio (#5304)
- Avoid overwriting '__module__' of messages from shared modules. (#5364)
- Attempt again to reproduce #4264. (#5403)
- Fix bad trove classifier

## 1.6.0

### Implementation changes

- Don't check `exclude_from_indexes` for empty lists. (#4915)

### Dependencies

- The minimum version for `google-api-core` has been updated to version 1.0.0. This may cause some incompatibility with older google-cloud libraries, you will need to update those libraries if you have a dependency conflict. (#4944, #4946)

### Testing and internal changes

- Install local dependencies when running lint (#4936)
- Re-enable lint for tests, remove usage of pylint (#4921)
- Normalize all setup.py files (#4909)
- Exercise datastore query result paging (#4905)
- Pass `*session.posargs` through on command line for system tests. (#4904)

## 1.5.0

### Interface additions

- Added `Entity.id` property (#4640)
- Added optional `location_prefix` kwarg in `to_legacy_urlsafe` (#4635)
- Added support for transaction options (#4357)
- Added the ability to specify read consistency (#4343, #4376)

### Implementation changes

- The underlying autogenerated code was rengereated to pick up new features and bugfixes. (#4348, #4877)
- Updated the HTTP implementation to match the gRPC implementation. (#4388)
- Set `next_page_token` to `None` if there are no more results (#4349)

### Documentation

- Entity doc consistency (#4641)
- Fixing "Fore" -> "For" typo in README docs. (#4317)

### Testing

- Update datastore doctests to reflect change in cursor behavior. (#4382)
- Making a `nox -s default` session for all packages. (#4324)
- Shorten test names (#4321)


## 1.4.0

### Interface changes / additions

- Allowing `dict` (as an `Entity`) for property values. (#3927)

### Documentation

- Added link to "Python Development Environment Setup Guide" in
  project README (#4187, h/t to @michaelawyu)

### Dependencies

- Upgrading to `google-cloud-core >= 0.28.0` and adding dependency
  on `google-api-core` (#4221, #4280)

PyPI: https://pypi.org/project/google-cloud-datastore/1.4.0/
