# etd-base-template
python template for etd projects

<img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/cgoines/68bd7e7d15e4025d7bf71431bad92771/raw/covbadge.json">

# Template Quickstart


# Badge Quickstart

For each new repository created with this you will need to do the following. 

## Create a Personal Access Token 
- Go to https://github.com/settings/tokens and create a Personal Access Token (classic). 
- Click “Generate new token.” 
- Select the “gist” scope, and click “Generate token.” 
- Copy the value displayed, it will begin with “ghp_”. You can’t get the value again, so be sure to save it somewhere.

NOTE: You may use the same Personal Access Tokens for multiple repositories so you do not have to do this step each time.
  
## Create Secret Gist

- Go to https://gist.github.com and make an empty secret gist.
- Name it the same as the repository you will be using it for.

NOTE: It may not allow you to leave it empty so any text in the body will do.  This is just a placeholder so the code knows where to create the badge json.

## Repository Settings

In your repository on GitHub that will be using the badge:
- Go to Settings - Secrets - Actions
- Click “New repository secret.” 
- Call the secret “GIST_TOKEN” 
- Paste the "ghp_" Personal Access Token token as the secret
- Click “Add secret”

## Workflow Settings

In your repository, open .github/workflows/pytest.yml
- Under the "Make badge" section, set the gistID = the ID of the gist that you created above.  It will be unique ID that can be found in the address bar of the gist.  For example, the address bar may look like:

https://gist.github.com/<userID>/1234513399189da4ff780f263984506c

1234513399189da4ff780f263984506c is the unique Gist ID.

## Readme Update

The badge URL (at the top of all READMEs using this template) must be updated in the README to use your newly created Gist.  The format is:
https://gist.githubusercontent.com/<your user id>/<unique Gist ID>/raw/covbadge.json 

The covbadge.json gets generated under the gist during the Git Action build.  This step points the image to the correct badge.

### References

- Coverage badge adapted from [Ned Batchelder](https://nedbatchelder.com/blog/202209/making_a_coverage_badge.html)
