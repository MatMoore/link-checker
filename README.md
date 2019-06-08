# Link checker

Some tools for checking lists of links.

## URL recorder
This script stores URLs in a Google Cloud Firestore database.

### Configuration
Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of a [Google Cloud Service Account Credentials File](https://cloud.google.com/docs/authentication/getting-started).

### How to run
`pipenv run python url_recorder.py INPUT_FILE`