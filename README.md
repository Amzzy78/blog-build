![logo]()

Welcome to Bia Simplí,

In this Blog application with Django it allows users to create, edit, and delete posts. The homepage will list all blog posts, and there will be a dedicated detail page for each individual post. 

Setting Up The Project
In the workspace I created a directory called mysite.
Then created an app named blog in the project.
The informed Django that a new application has been created, opening the settings.py file and added to the installed apps section, which  already has installed apps.
Then performed make migrations. This applied all the unapplied migrations on the SQLite database which comes along with the Django installation.

https://djangocentral.com/building-a-blog-application-with-django/

Edit this turtorial 

Database Models
I defined the data models for the blog. A model is a Python class that subclasses django.db.models.Model, in which each attribute represents a database field. Using this subclass functionality, we automatically have access to everything within django.db.models.Models and can add additional fields and methods as desired. We will have a Post model in our database to store posts.

At the top, we’re importing the class models and then creating a subclass of models.Model Like any typical blog, each blog post will have a title, slug, author name, and the timestamp or date when the article was published or last updated.

Notice how we declared a tuple for STATUS of a post to keep draft and published posts separated when we render them out with templates.

The Meta class inside the model contains metadata. We tell Django to sort results in the created_on field in descending order by default when we query the database. We specify descending order using the negative prefix. By doing so, posts published recently will appear first.

The __str__() method is the default human-readable representation of the object. Django will use it in many places, such as the administration site.

Now that our new database model is created we need to create a new migration record for it and migrate the change into our database.

Creating An Administration Site
We will create an admin panel to create and manage Posts. Fortunately, Django comes with an inbuilt admin interface for such tasks.
In order to use the Django admin first, we need to create a superuser by running the following command in the prompt.
You will be prompted to enter email, password, and username. Note that for security concerns Password won't be visible.

Enter any details you can always change them later. After that rerun the development server and go to the address http://127.0.0.1:8000/admin/

You should see a login page, enter the details you provided for the superuser.

After you log in you should see a basic admin panel with Groups and Users models which come from Django authentication framework located in django.contrib.auth.

Still, we can't create posts from the panel we need to add the Post model to our admin.

Adding Models To The Administration Site
Open the blog/admin.py file and register the Post model there as follows.

Now let's create our first blog post click on the Add icon beside Post which will take you to another page where you can create a post. Fill the respective forms and create your first ever post.

Once you are done with the Post save it now, you will be redirected to the post list page with a success message at the top.

Though it does the work, we can customize the way data is displayed in the administration panel according to our convenience

This will make our admin dashboard more efficient. Now if you visit the post list, you will see more details about the Post.

Note that I have added a few posts for testing.

The list_display attribute does what its name suggests display the properties mentioned in the tuple in the post list for each post.

If you notice at the right, there is a filter which is filtering the post depending on their Status this is done by the list_filter method.

And now we have a search bar at the top of the list, which will search the database from the search_fields attributes. The last attribute prepopulated_fields populates the slug, now if you create a post the slug will automatically be filled based upon your title.

Now that our database model is complete we need to create the necessary views, URLs, and templates so we can display the information on our web application.

Building Views
A Django view is just a Python function that receives a web request and returns a web response. We’re going to use class-based views then map URLs for each view and create an HTML templated for the data returned from the views.

Open the blog/views.py file and start coding.

The built-in ListViews which is a subclass of generic class-based-views render a list with the objects of the specified model we just need to mention the template, similarly DetailView provides a detailed view for a given object of the model at the provided template.

Note that for PostList view we have applied a filter so that only the post with status published be shown at the front end of our blog. Also in the same query, we have arranged all the posts by their creation date. The ( - ) sign before the created_on signifies the latest post would be at the top and so on.

Adding URL patterns for Views
We need to map the URL for the views we made above. When a user makes a request for a page on your web app, the Django controller takes over to look for the corresponding view via the urls.py file, and then return the HTML response or a 404 not found error, if not found.

Create an urls.py file in your blog application directory and add the following code.

We mapped general URL patterns for our views using the path function. The first pattern takes an empty string denoted by ' ' and returns the result generated from the PostList view which is essentially a list of posts for our homepage and at last we have an optional parameter name which is basically a name for the view which will later be used in the templates.

Names are an optional parameter, but it is a good practice to give unique and rememberable names to views which makes our work easy while designing templates and it helps keep things organized as your number of URLs grows.

Next, we have the generalized expression for the PostDetail views which resolve the slug (a string consisting of ASCII letters or numbers) Django uses angle brackets < > to capture the values from the URL and return the equivalent post detail page.

Now we need to include these blog URLs to the actual project for doing so open the mysite/urls.py file.

Now all the request will directly be handled by the blog app.

Creating Templates For The Views
We are done with the Models and Views now we need to make templates to render the result to our users. To use Django templates we need to configure the template setting first.

Create directory templates in the base directory. Now open the project's settings.py file and just below BASE_DIR add the route to the template directory as follows.

Now add the newly created TEMPLATE_DIRS  in the DIRS.

Now save and close the file we are done with the configurations.

Django makes it possible to separate python and HTML, the python goes in views and HTML goes in templates. Django has a powerful template language that allows you to specify how data is displayed. It is based on template tags, template variables, and template filters.

I'll start off with a base.html file and a index.html file that inherits from it. Then later when we add templates for homepage and post detail pages, they too can inherit from base.html.

Let's start with the base.html file which will have common elements for the blog at any page like the navbar and footer. Also, we are using Bootstrap for the UI and Roboto font

This is a regular HTML file except for the tags inside curly braces { } these are called template tags.

The {% url 'home' %} Returns an absolute path reference, it generates a link to the home view which is also the List view for posts.

The {% block content %} Defines a block that can be overridden by child templates, this is where the content from the other HTML file will get injected.

Next, we will make a small sidebar widget which will be inherited by all the pages across the site. Notice sidebar is also being injected in the base.html file this makes it globally available for pages inheriting the base file.

Next, create the index.html file of our blog that's the homepage.

With the {% extends %} template tag, we tell Django to inherit from the base.html template. Then, we are filling the content blocks of the base template with content.

Notice we are using for loop in HTML that's the power of Django templates it makes HTML Dynamic. The loop is iterating through the posts and displaying their title, date, author, and body, including a link in the title to the canonical URL of the post.

In the body of the post, we are also using template filters to limit the words on the excerpts to 200 characters. Template filters allow you to modify variables for display and look like {{ variable | filter }}.

Now run the server and visit http://127.0.0.1:8000/ you will see the homepage of our blog.

You might have noticed I have imported some dummy content to fill the page you can do the same using this lorem ipsum generator tools.

Now let's make an HTML template for the detailed view of our posts.

Next, Create a file post_detail.html and paste the below HTML there.

At the top, we specify that this template inherits from.base.html Then display the body from our context object, which DetailView makes accessible as an object.

Now visit the homepage and click on read more, it should redirect you to the post detail page.

Creating Comments System With Django
Let readers add comments on posts.

Roadmap To Build A Comment System
1. Create a model to save the comments.
2. Create a form to submit comments and validate the input data.
3. Add a view that processes the form and saves the new comment to the database.
4. Edit the post detail template to display the list of comments and the form to add a new comment.


Adding Pagination With Django


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
