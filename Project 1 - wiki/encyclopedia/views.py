from django.shortcuts import render
import markdown
import random

from . import util

def convert_from_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    # Check if file exists
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content_html = convert_from_md_to_html(title)
    # Check if file exists
    if content_html == None:
        return render(request, "encyclopedia/error.html", {
            "error_message": "This entry doesn't exist.."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content_html,
        })

def search(request):
    message = ""
    search_query = request.GET['q']
    content_html = convert_from_md_to_html(search_query)
    if content_html is not None:
        return render(request, "encyclopedia/entry.html", {
            "title": search_query,
            "content": content_html,
    })
    else:
        # Creating a list containing the words matching the letters in the input search
        every_entries = util.list_entries()
        results = []

        for entry in every_entries:
            # Converting everything to lower to avoid any mismatching by lower or Maj
            if search_query.lower() in entry.lower():
                results.append(entry)

        # Checking if the list if empty, if yes, send error message
        if len(results) == 0:
            message = "Your search doesn't match any entry. Please retry."
        return render(request, "encyclopedia/search_query.html", {
                "results": results,
                "message": message,
        })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    
    # If method is Post
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleAlreadyExist = util.get_entry(title)

        # If title already exist
        if titleAlreadyExist is not None:
            return render(request, "encyclopedia/error.html", {
                "error_message": "This entry already exists!"
            })
        else:
            util.save_entry(title, content)
            content_html = convert_from_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": content_html,
            })

def edit_page(request):
    if request.method == "POST":
        title = request.POST['title_selected']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": content,
        })

def save_edited_page(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        content_html = convert_from_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content_html,
        })
        
def random_page(request):
    every_entries = util.list_entries()
    random_choice = random.choice(every_entries)
    content_html = convert_from_md_to_html(random_choice)
    return render(request, "encyclopedia/entry.html", {
        "title": random_choice,
        "content": content_html,
    })

def delete_page(request):
    if request.method == "POST":
        title = request.POST['title_to_delete']
        content = util.get_entry(title)
        util.delete_entry(title, content)
    return render(request, "encyclopedia/delete.html", {
        "message": "Page deleted successfully!"
    })