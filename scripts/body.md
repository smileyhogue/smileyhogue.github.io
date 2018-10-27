# Introduction
This page provides some basic information about using your GitHub account to create static websites with GitHub Pages. Using GitHub pages is great because anything you can create with static HTML, CSS, and JavaScript can easily be made available to others on the web. 

Take this for what is it: an example illustrating just one of a myriad of ways to accomplish the goal of getting your work online. I made decisions about what technologies and services to use motivated by a desire to control my content and take advantage of free services, but you can find many easier[^easier]—or just different—solutions to meet your preferences.

[^easier]: Yes, building a static website can be frustrating while you learn how to do so: Vicki Boykis, “Man, do static sites suck,” Vicki Boykis's Blog, May 30, 2015, [http://veekaybee.github.io/2015/05/30/static-sites-suck/](http://veekaybee.github.io/2015/05/30/static-sites-suck/).

This page is written in [Markdown](https://daringfireball.net/projects/markdown/), converted to HTML with [Markdown2](https://github.com/trentm/python-markdown2), generated with [Python](https://www.python.org/), and hosted on [GitHub pages](https://pages.github.com/). The source code is available here: [https://github.com/mkudija/GitHub-Pages-Example](https://github.com/mkudija/GitHub-Pages-Example)


# 1. Set Up GitHub Pages
The first step is to set up a GitHub repository to host the files for your website. You can create your GitHub account [https://github.com/join](https://github.com/join). 

Any repository can be the source for GitHub Pages. First create a new repository:

<center><img src="images/gh-pages-1.png"></center>

Next we can configure GitHub Pages. The [GitHub Pages welcome page](https://pages.github.com/) has simple instructions, or follow along below. You can choose the location of the source files to be either the root of the master branch, or the docs folder in the master branch. I usually just choose the root of the master branch:

<center><img src="images/gh-pages-2.png"></center>

If set up properly you will be provided the link for your page:

<center><img src="images/gh-pages-3.png"></center>


Since we have not yet committed any source files for our webpage to the master branch, nothing is shown. The next steps will walk through building the website.

<center><img src="images/gh-pages-4.png"></center>


# 2. Build the Website

If you are comfortable doing so yourself you can jump right in and write the HTML, CSS, and JavaScript (if necessary) files to run your site. These details are beyond the scope of this overview but there are plenty of resources online.

If not, you're still in luck. Just use one of the many free templates to be found online and add your content and any stylistic tweaks you want to make. [HTML5UP](https://html5up.net/) has a number free, excellent, responsive templates available licensed under the Creative Commons Attribution 3.0 License. There are also multiple [Python-powered static site generators](https://www.fullstackpython.com/static-site-generator.html) ([Pelican](https://blog.getpelican.com/), [Hyde](http://hyde.github.io/), etc.) that have pre-built themes available for use or customization.

Styling the site can be a black hole of tinkering, but some easier items to update include colors and typeface.


<div class="info box"><strong>Info!</strong> A rookie mistake I made and that you can avoid is thinking that you need to commit your changes to GitHub each time to see how they look. Simply open the file locally (right click on <code>index.html</code> and open in Chrome) and as soon as changes are saved you can refresh the page to view the result. In Safari you can go to <strong>Develop</strong> > <strong>Enter Responsive Design Mode</strong> to see how your website will render on various screen sizes.</div>


<div class="info box"><strong>Info!</strong> If you see something online you like and want to incorporate into your website, from Chrome right click and select <strong>Inspect</strong> to reveal the source code. This is a great way to learn about how other websites are built.</div>


# 3. Add Extras

Now that you are up and running with a basic static website, here are some optional "extras" you may want to add.

## 404.html
The default 404 page on GitHub pages is pretty boring and not specific to your site. If you would like a 404 page to match your theme, you can add a custom [404.html](https://github.com/mkudija/mkudija.github.io/blob/master/404.html) to your root directory.


## CNAME
If you want a custom domain (i.e. `matthewkudija.com` instead of `mkudija.github.io`), perform the following:
1. Buy the domain from your preferred DNS provider. I use Host Gator.
2. Add a [CNAME](CNAME) file to your directory. This should contain just the domain: `matthewkudija.com`. 
3. Contact your DNS provider to point to GitHub pages. Refer to the [documentation](https://help.github.com/articles/setting-up-an-apex-domain/).


## favicon.ico
The favicon is the small image displayed on the tab in your web browser. You can create or find a square image to use as your favicon. Go to one of the many favicon generator sites (such as [this](https://realfavicongenerator.net/)) to generate your favicon and upload this to the root directory of your website named `favicon.ico`.

## sitemap.xml
You can add a sitemap to aid in searching (and perhaps eventually get sitelinks on the search result) from [xml-sitemaps.com](https://www.xml-sitemaps.com). This also gets uploaded to the root directory of your webiste.

## Meta tags
To improve search results, you can update the meta tags. See more information about [meta tags that Google understands](https://support.google.com/webmasters/answer/79812?hl=en). Two examples include `"description"` and `"keywords"`:


```html
<meta name="description" content="add a description of your site here">
<meta name="keywords" content="add, some, keywords, you, want, here">
```

## Google Analytics
To analyze traffice to your website, set up [Google Analytics](https://analytics.google.com/analytics/web/) to get your unique tracking ID and then copy the required code in to your HTML pages.

```html
  <!-- Global Site Tag (gtag.js) - Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-<YOUR ID>"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-<YOUR ID>');
  </script>
```


# 4. Auto Build Your Site

If you site is truly static is may be reasonable to write it all in HTML and let it be. Likely, you will have dynamic content (images, dates, articles, tables, charts) to be updated frequently. In this case, some simple Python scripts can handle the rote data aggregation, chart generation, and assembly of the final HTML page(s). 

This page is generated from [build.py](scripts/build.py) which draws from a [template.html](scripts/_template.html) file, inserts the body of text from a [body.md](scripts/body.md) file, reads data from an [Excel](example-data.xlsx) file to populate a table, and updates the date in the footer.

For example, we can write a simple function to copy a file from one location to another and use it to copy the `template.html` to the live `index.html`. Likewise, another function can be used to insert live HTML snippets into this template. Combining a few simple functions like this we can update a website of moderate complexity with little to no marginal effort.

As one example of this, we can read an Excel file into a Pandas DataFrame, drop that into an HTML table, and use some JavaScript to make the table filterable on the page (this data comes from the Wikipedia page for the [List of Solar System objects by size](https://en.wikipedia.org/wiki/List_of_Solar_System_objects_by_size)): 

XXX-INSERT TABLE HERE-XXX

# Conclusion

This is a brief overview and example of what you can build with GitHub pages. Feel free to submit a pull request with any additions or <A HREF="mailto:m.kudija@gmail.com">contact me</A> with questions, suggestions, or other examples.
