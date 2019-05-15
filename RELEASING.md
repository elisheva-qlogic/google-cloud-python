
## Dependencies
1. Install releasetool. [Releasetool](https://github.com/googleapis/releasetool/) requires Python >= 3.6.
    ```
    python3 -m pip install gcp-releasetool
    ```
## Steps

The steps below assume you are releasing `vision`. Replace `vision` with the library you are releasing.

1. Checkout master, pull from the remote, and fetch tags. 
   
   **Note**: These steps assume you've forked this repo and have a remote named `upstream` pointing to `googleapis/google-cloud-python` 
   Adjust the commands accordingly if you have a different setup.
   ```
   git checkout master
   git pull upstream master
   git fetch --tags
   ```
2. Go to the library directory and run releasetool start.
   ```
   cd vision
   python3 -m releasetool start
   ```
3. Releasetool opens the release notes in a text editor. Categorize the commit messages and save the file.
4. Releasetool asks for the update type. Use [Semantic Versioning](https://semver.org).
    
    Given a version number **MAJOR**.**MINOR**.**PATCH**, increment the:
    * **MAJOR** version when you make incompatible API changes,
    * **MINOR** version when you add functionality in a backwards-compatible manner, and
    * **PATCH** version when you make backwards-compatible bug fixes.
5. Releasetool creates a branch `release-vision-x.x.x`. Releasetool pushes the branch to GitHub and a PR is created.
Releasetool adds the label `autorelease: pending` so that the Autorelease bot can find the pull request.
6. Get the PR reviewed and merged.
7. After the PR is merged, the Autorelease bot will find it and finish out the release process. The Autorelease bot runs every 15 minutes
7AM-6PM PT M-F.
