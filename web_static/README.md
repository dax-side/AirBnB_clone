# AirBnB Clone - Web Static
In this project I will be building the frontend of the AirBnB clone step-by-step
The first step is to `design`/ `sketch`/`protoytpe`each element:
- Create simple HTML static pages
- Style guide
- Fake Contents
- No Javascript
- No data loaded from anything
During this project, I will learn how to manipulate HTML and CSS. HTML is the structure of the page.
CSS is the styling of the page, the design.
## Task 0
* **Inline styling**
[0-index.html](./0-index/html): HTML page that displays a header and footer.
<h3>Layout</h3>
<ul>
	<li>Body
		<ul>
			<li>no margin</li>
			<li>no padding</li>
		</ul>
	</li>
<li>Header
	<ul>
		<li>color #FF0000 (red)</li>
		<li>height: 70px</li>
		<li>width: 100%</li>
	</ul>
</li>
<li>Footer
	<ul>
		<li>color #00FF00 (green)</li>
		<li>height: 60px</li>
		<li>width: 100%</li>
		<li>text <b>Best School</b> center vertically and horizontally</li>
		<li>always at the bottom of the page</li>
	</ul>
</li>
</ul>
<h3>Requirements:</h3>
<ul>
	<li>Use the <b>header</b> and <b>footer</b> tags</li>
	<li>Importing any files is not allowed</li>
	<li>Use of the <b>style</b> tag in the <b>head</b> tag is not allowed</li>
	<li>Inline styling should be used for all tags</li>
	<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
</ul>

## Task 1
* **Head styling**
[1-index.html](./1-index.html): HTML page that displays a header and footer by using the `style` tag in the `head` tag (same as `0-index.html`)
<h3>Requirements:</h3>
<ul>
	<li>Use the <b>header</b> and <b>footer</b> tags</li>
	<li>Importing any files is not allowed</li>
	<li>No inline styling</li>
	<li>The <b>style</b> tag must be used in the <b>head</b> tag </li>
</ul>

## Task 2
* **CSS files**
[2-index.html](./2-index.html): HTML page that displays a header and footer by using CSS files (same as `1-index.html`)
<h3>Requirements</h3>
<ul>
	<li>Use the <b>header</b> and <b>footer</b> tags</li>
	<li>No inline styling</li>
	<li>Use 3 CSS files:	
		<ul>
			<li><a href="./styles/2-common.css">styles/2-common.css: </a>for global style(i.e. the body style)</li>
			<li><a href="./styles/2-header.css">styles/2-header.css: </a>for header style</li>
			<li><a href="./styles/2-footer.css">styles/2-footer.css: </a>for footer style</li>
			<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
		</ul>
	</li>
</ul>

## Task 3
* **Zoning done!**
[3-index.html](./3-index.html): HTML page that displays a header and footer by using CSS files (same as `2-index.html`)
<h2>Layout</h2>
<ul>
	<li>Common:
		<ul>
			<li>no margin</li>
			<li>no padding</li>
			<li>font color: #484848/li>
			<li>font size: 14px</li>
			<li>font family: Circular, "Helvitica Neue", Helvitica, Aria, sans-serif;</li>
			<li>icon in the browser tab</li>
		</ul>
	</li>
	<li>Header:
		<ul>
			<li>color: white</li>
			<li>height: 70px</li>
			<li>width: 100%</li>
			<li>border bottom 1px #CCCCCC</li>
			<li>logo align on left and center vertically (20px space at left</li>
		</ul>
	</li>
	<li>Footer:
		<ul>	
			<li>color: white</li>
			<li>height: 60px</li>
			<li>width: 100%</li>
			<li>border top 1px #CCCCCC</li>
			<li>text <b>Best School</b> center vertically and horizontally</li>
			<li>always at the bottom of the page</li>
		</ul>
	</li>
</ul>
<h3>Requirements</h3>
<ul>
	<li>No inline styling</li>
	<li>Use of the <b>img</b> tag is not allowed</li>
	<li>Use of the <b>style</b> tag in the <b>head</b> tag is not allowed</li>
	<li>All images must be stored in the images folder</li>
	<li>Use 3 CSS files:	
		<ul>
			<li><a href="./styles/3-common.css">styles/3-common.css: </a>for global style(i.e. the body style)</li>
			<li><a href="./styles/3-header.css">styles/3-header.css: </a>for header style</li>
			<li><a href="./styles/3-footer.css">styles/3-footer.css: </a>for footer style</li>
			<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
		</ul>
	</li>
</ul>

## Task 4
* **Search**
[4-index.html](./4-index.html): HTML page that displays a header, footer and a filters box with a search button.
<h2>Layout</h2>
<p>Based on 3-index.html</p>
<ul>
	<li>Container:
		<ul>
			<li>between <span style="color:red">header</span> and <span style="color:red">footer</span> tags, add a <span style="color:red">div</span>: 
				<ul>
					<li>classname: <span style ="color:red">container</span></li>
					<li>max width: 1000px</li>
					<li>margin top and bottom 30px- should be 30px under the bottom of the <span style="color:red">header</span></li>
					<li>center horizontally</li>
				</ul>
			</li>
		</ul>
	</li>
	<li> Filter section:
		<ul>
			<li>tag <span style="color:red">section</span></li>
			<li>classname: <span style="color:red">filters</span></li>
			<li>inside the <span style="color:red">.container</li>
			<li>color: white</li>
			<li>height: 70px</li>
			<li>width: 100% of the container</li>
			<li>border: 1px solid #DDDDDD with radius 4px</li>
		</ul>
	</li>
	<li> Button Search:
		<ul>	
			<li>tag <span style="color:red">button</span></li>
			<li>text <span style="color:red">search</span></li>
			<li>font size: 18px</li>
			<li>inside the section filters</li>
			<li>background color #FF5A5F</li>
			<li>text color #FFFFFF</li>
			<li>height: 48px</li>
			<li>width: 20% of the section filters</li>
			<li>no borders</li>
			<li>border radius: 4px</li>
			<li>center vertically and at 30px of the right border</li>
			<li>change opacity to 90% when the mouse is on the button</li>
		</ul>
	</li>
</ul>
<h3>Reuirements</h3>
<ul>
	<li>Use the: header, footer, section, button tags</li>
	<li>No inline style</li>
	<li>img tag is not allowed</li>
	<li>Use of the style tag in the head tag not allowed</li>
	<li>All images must be stored in the images folder</li>
	<li>Use 4 CSS files:
		<ul>
			<li><a href="./styles/4-common.css">styles/4-common.css: </a>for global style(i.e. the body and .container styles)</li>
			<li><a href="./styles/4-header.css">styles/4-header.css: </a>for header style</li>
			<li><a href="./styles/4-footer.css">styles/4-footer.css: </a>for footer style</li>
			<li><a href="./styles/4-filters.css">styles/4-filters.css: </a>for filters style</li>
			<li>Not <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
</ul>
