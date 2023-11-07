import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


# Return list of all the encyclopedia entries.
def list_entries():
    _, filenames = default_storage.listdir("entries")
    # return data of list enties and the file name end with .md;
    return list(
        sorted(
            re.sub(r"\.md$", "", topicname)
            # the title in the list which the file extention end with .md;
            for topicname in filenames
            if topicname.endswith(".md")
        )
    )


#  Store encyclopedia entry with title and Markdown content and it will replaceexisting entries
def save_entry(title, content_entry):
    # store data in toppicname with title.
    topicname = f"entries/{title}.md"
    # if the topic name is already existing, then replace the old one.
    if default_storage.exists(topicname):
        default_storage.delete(topicname)
    # Store new topic data
    default_storage.save(topicname, ContentFile(content_entry))


# Retrieves any encyclopedia entries by title If entry si not existing then returns None.
def get_entry(title):
    # directly try first. store data in "files_sotre"
    try:
        files_sotre = default_storage.open(f"entries/{title}.md")
        return files_sotre.read().decode("utf-8")
    except FileNotFoundError:
        return None


# Clicking on any of the entry names on the search results page should take the user to that entry’s page.
# # Searche topics that allready have been created in the encyclopedia by topics title.
def search(searchquery):
    # sotre data in the filenames.
    _, filenames = default_storage.listdir("entries")
    # return the list that stored and the file name end with .md;
    return list(
        sorted(
            re.sub(r"\.md$", "", topicname)
            #  title in the filenames which are file entention end with .md;
            for topicname in filenames
            if topicname.endswith(".md") and searchquery.lower() in topicname.lower()
        )
    )
