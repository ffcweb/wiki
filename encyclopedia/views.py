from unittest import loader
from django import template
from django.http import HttpResponse
from django.shortcuts import render
from . import util
from random import choice
from django.shortcuts import render, redirect
from markdown2 import markdown
from django.contrib import messages


# Index Page: Update index.html such that, instead of merely listing the names of
# all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page.
def index(request):
    #  A page listted all entries: return index.html page and list all the the entries
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


# Entry Page: Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
# The view should get the content of the encyclopedia entry by calling the appropriate util function.
# If an entry is requested that does not exist, the user should be presented with an error messages page indicating that their requested page was not found.
# If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.
def entry(request, title):
    # When user research an entry for contents:
    # Sotre dada in content, if content is None, the content will be a massage to user.
    content_entry = util.get_entry(title.strip())
    if content_entry is None:
        return render(request, "encyclopedia/404.html")
    # If that content page can be found, then get the content transfered to markdown format
    # and store data in variable "content", then return the entry.html page.
    content_entry = markdown(content_entry)
    # Markdown to HTML Conversion: On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via pip3 install markdown2.
    return render(
        request, "encyclopedia/entry.html", {"title": title, "entry": content_entry}
    )


# Search: Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry.
# If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.
# If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results.
# Clicking on any of the entry names on the search results page should take the user to that entry’s page.
def search(request):
    # Loads user requested content accrording the title user typing, if it not exists
    # then give a string to tell user.
    # store data in query, if the title can be found lead to that entry page.
    # Remove spaces at the beginning and at the end of the string:
    search_query = request.POST.get("q", "").strip()
    search_query = search_query.upper()
    # if requested topic that is in the exits, return the topic by title
    if search_query in util.list_entries():
        return redirect("entry", title=search_query)
    # matchs relevant letters for the searching.
    return render(
        request,
        "encyclopedia/search.html",
        {"entries": util.search(search_query), "search_query": search_query},
    )


# Create New Page: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
# Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.
# Users should be able to click a button to save their new page.
# When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error messages message.
# Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.
def create(request):
    if request.method == "POST":
        # Remove spaces at the beginning and at the end of the string:
        title = request.POST.get("title").strip()
        title = title.upper()
        content_entry = request.POST.get("content_entry").strip()
        if title in util.list_entries():
            return render(
                request,
                "encyclopedia/create.html",
                {"messages": "This title is already existting!"},
            )
        elif title == "" or content_entry == "":
            return render(
                request,
                "encyclopedia/create.html",
                {"messages": "Type the title you want to see!"},
            )
        util.save_entry(title, content_entry)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/create.html")


# Edit an existing page: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
# The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
# The user should be able to click a button to save the changes made to the entry.
# Once the entry is saved, the user should be redirected back to that entry’s page.
def edit(request, title):
    # store in the content variable
    # Remove spaces at the beginning and at the end of the string:
    content_entry = util.get_entry(title.strip())
    # content_entry = content_entry.capitalize()
    # if there is no matching result, then return a message that says page not found.
    if content_entry is None:
        return render(request, "encyclopedia/404.html")
    # if content entry is empty , then return a message that says Not successed!
    if request.method == "GET":
        # Remove spaces at the beginning and at the end of the string:
        content_entry = request.GET.get("content_entry").strip()
        if content_entry == "":
            return render(request, "encyclopedia/404.html")
        util.save_entry(title, content_entry)
        # redirect to the titles
        return redirect("entry", title=title)
    # redirect to the edit.html
    return render(
        request,
        "encyclopedia/edit.html",
        {"content_entry": content_entry, "title": title},
    )


# return the 404 page.
def handler404(request, *args):
    return render(request, "404.html", {})


# Random Page: Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
# Search pages randomly:
def random(request):
    # store data in entries
    entries = util.list_entries()
    # redirect user to a random page that title is equal to choice(entries).
    return redirect("entry", title=choice(entries))
