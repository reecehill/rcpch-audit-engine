import os


def export_vars(request):
    """
    Gets the `GIT_HASH` environment variable, created in GitHub Actions workflow, inserts into all templates.
    """
    # Load the txt file containing hash
    try:
        with open('git_hash.txt', 'r') as f:

            git_branch, git_hash = f.read().split(',')

            git_hash = git_hash.replace('GIT_HASH=', '')
            git_branch = git_branch.replace('GIT_BRANCH=', '')

            # if file is empty
            if not git_hash:
                git_hash = 'Empty commit file'

    except FileNotFoundError:
        git_hash = 'No commit hash found! Ignore if running locally.'
        git_branch= 'No branch found!'
    return {'GIT_HASH': git_hash, 'GIT_BRANCH': git_branch}
