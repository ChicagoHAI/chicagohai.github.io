# Chicago HAI Homepage

Repository for [Chicago Human+AI homepage](https://chicagohai.github.io/). The homepage is based on Hugo static site generator and [Researcher theme](https://github.com/ojroques/hugo-researcher).

## Developing

### Clone

First, clone the repo.

```bash
git clone --recurse-submodules https://github.com/ChicagoHAI/chicagohai.github.io.git
```

> [!TIP]
> If you don't need to edit the homepage **theme**, but just change people information or post news, you don't need to clone with `--recurse-submodules`.

Currently we are using the `dev` branch as the main branch.

> [!WARNING]
> **Do not** push and pull to `github-pages` branch. It's handled by GitHub Actions automatically.


### Edit

You don't need [Hugo](https://gohugo.io/) installed on your local machine to edit the content. Just edit the markdown files in `content/` and `data/` folders, check [content](#Content) for more details on this.

If you want to preview the website locally, you need to install Hugo. See [Environments](#Environments) for more details.

### Commit and push

Commit your changes and push it to the remote server on GitHub. A push will trigger GitHub Actions to build the website automatically. You don't need to and shouldn't commit the `public/` folder.

You can check the progress on the [Workflows log page](https://github.com/ChicagoHAI/chicagohai.github.io/actions/workflows/build.yml). After it's done, GitHub Pages will [automatically deploy it](https://github.com/ChicagoHAI/chicagohai.github.io/actions/workflows/pages/pages-build-deployment). Wait for some time and then refresh the homepage, and it's done. You may need to manually clear the cache.

## Environments

An earlier version of installing instructions can be found in [README.legacy.md](README.legacy.md).

### Install Hugo

You don't need to install [Golang toolchain](https://golang.org/) to use Hugo site generator. Check their [installation guide](https://gohugo.io/installation/) for more details.

> [!TIP]
> If you are on Mac, you can use [Homebrew](https://brew.sh/) to install Hugo.
> ```bash
> brew install hugo
> ```
>
> If you are on Windows, you can use [Scoop](https://scoop.sh/) to install Hugo.
> ```powershell
> scoop install hugo
> ```

### Run server

Run the following command in the base directory of this repo.

```bash
hugo server
```

Then you can preview the website on `localhost:1313`. The server will automatically reload when you change the content.

### Build

> [!IMPORTANT]
> You **don't need to and shouldn't** build the website manually. GitHub Actions will build it automatically.

## Contents

### Add your information

The people data is stored in [`data/people.yaml`](https://github.com/ChicagoHAI/chicagohai.github.io/blob/dev/data/people.yaml). You can add your information to this YAML file under the right section (phd, postdoc, masters and undergrads etc.).

```yaml
- id: john_doe # last-name_first-name is preferred. Use underscore to connect.
  name: John Doe
  homepage: https://chicagohai.github.io/ # Optional. Omit the key-value pair if you don't have one.
```

If you are using VSCode, this file should have an auto type check.

### Add your avatar

The avatars are stored in [`assets/images/people`](https://github.com/ChicagoHAI/chicagohai.github.io/blob/dev/asset/images/people). Crop your avatar to 1x1 ratio (the size doesn't matter) and **rename it to your id** you set in the `people.yaml` file. You can use JPG or PNG format. Put your avatar inside the folder.

### Add your publication and demos

Edit [`content/demos.yaml`](content/demos.yaml) and [`content/publications.yaml`](content/publications.yaml) to add your demos and publications. These are normal Markdown files.

### Add news

News are stored in [`content/news/`](content/news). Add a new Markdown file to this folder to add a news. We recommend to use the format of `YYMMDD-{title}.md` for news files, so the files will be ordered by time without sorting. The content of the file should start with [TOML frontmatter](https://gohugo.io/content-management/front-matter/#front-matter-formats) like this:

```markdown
+++
title = "Postdoc Position through DSI Fellowship"
date = 2022-07-22
contentAsDesc = true
+++
```

Refer to [TOML help](https://toml.io/en/) for more details on TOML format.

The `contentAsDesc` field is used to show the content of the news as the description on the news list page. You can manually add a `description` field to the frontmatter to override this behavior, as in [the symposium post](content/news/230813-symposium-hai/index.md).

If you need LaTeX support on the post, add `math = true` to the frontmatter.

If you need to add images to the post, move the Markdown file to a folder of name `YYMMDD-{title}` and rename the Markdown file to `_index.md`. Images can be stored inside this folder and its subfolders. For example, if you put an image at `./images/1.png`, you can refer to it in the Markdown file as `![image](images/1.png)`.

There are some [Hugo shortcodes](https://gohugo.io/content-management/shortcodes/) you can use on the news post. Check [Shortcodes](#Shortcodes) for more details.

## Shortcodes

### `card`

A colored background to emphasize some content.

```markdown
{{% card %}}
This is the content of the card.
{{% /card %}}
```

### `grid`

A easy way to create a grid. By default, it will create a grid with 2 column and the second column will fill all remaining space. You can specify the number of columns by `cols` parameter using CSS's `grid-template-columns` syntax. You can also specify `rows` for `grid-template-rows`. `gap` is used to specify the gap between rows and columns. `style` can be used to specify other CSS styles.

```markdown
{{% grid gap="0 0.5rem" %}}
**(1,1)**

(1,2)

**(2,1)**

(2,2)
{{% /grid %}}
```

> [!TIP]
> For a 3 column grid, you can use `cols="auto auto 1fr"`.

> [!NOTE]
> In Hugo, you can `{{% shortcode %}}` and `{{% /shortcode %}}` to wrap Markdown contents and `{{< shortcode >}}` and `{{< /shortcode >}}` to wrap raw HTML contents.