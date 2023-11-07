# markdown cheat sheet

## thanks for visiting [the markdown guide](https://www.markdownguide.org)!

- this markdown cheat sheet provides a quick overview of all the markdown syntax elements. it can’t cover every edge case, so if you need more information about any of these elements, refer to the reference guides for [basic syntax](https://www.markdownguide.org/basic-syntax/) and [extended syntax](https://www.markdownguide.org/extended-syntax/).


## basic syntax

- these are the elements outlined in john gruber’s original design document. all markdown applications support these elements.

### heading

-   # h1
-   ## h2
-   ### h3

-   ### bold

-   **bold text**

### italic

-   *italicized text*

-   ### blockquote

-   > blockquote

### ordered list

1. first item
2. second item
3. third item

### unordered list

- first item
- second item
- third item

### code

-  `code`

### horizontal rule

-  ---

### link

-  [markdown guide](https://www.markdownguide.org)

### image

-  ![alt text](https://www.markdownguide.org/assets/images/tux.png)

## extended syntax

-  these elements extend the basic syntax by adding additional features. not all markdown applications support these elements.

### table

- | syntax | description |
- | ----------- | ----------- |
- | header | title |
- | paragraph | text |

### fenced code block

-  ```
- {
-  "firstname": "john",
-  "lastname": "smith",
-   "age": 25
- }
-  ```

### footnote

-  here's a sentence with a footnote. [^1]

-  [^1]: this is the footnote.

-  ### heading id

-  ### my great heading {#custom-id}

-  ### definition list

-  term
-  : definition

### strikethrough

-  ~~the world is flat.~~

-  ### task list

- [x] write the press release
- [ ] update the website
- [ ] contact the media

-  ### emoji

-  that is so funny! :joy:

-  (see also [copying and pasting emoji](https://www.markdownguide.org/extended-syntax/#copying-and-pasting-emoji))

### highlight

-  i need to highlight these ==very important words==.

### subscript

-  h~2~o

### superscript

-  x^2^

____