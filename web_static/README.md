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
Based on <a href="./3-index.html">3-index.html</a>
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

## Task 5
* **More filters**
[5-index.html](./5-index.html): HTML page that displays a header, footer and a filters box.
<h2>Layout</h2>
Based on <a href="./4-index.html">4-index.html</a>
<ul>
	<li>Location and Amenities filters:
		<ul>
			<li>tag: div</li>
			<li>classname: locations for location tag and amenities for the other</li>
			<li>inside the section filters(same level as the button Search)</li>
			<li>height: 100% of the section filters</li>
			<li>width: 25% of the section filters</li>
			<li>border right #DDDDDD 1px only for the first left filter</li>
			<li> Contains a title: 
				<ul>
					<li>tag: h3</li>
					<li>font weight: 600</li>
					<li>text States or Amenities</li>
				</ul>
			</li>
			<li> Contains a subtitle: 
				<ul>
					<li>tag: h4</li>
					<li>font weight: 400</li>
					<li>font size 14px</li>
					<li>text with fake contents</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<h3>Reuirements</h3>
<ul>
	<li>Use the: header, footer, section, button, h3, h4 tags</li>
	<li>No inline style</li>
	<li>img tag is not allowed</li>
	<li>Use of the style tag in the head tag not allowed</li>
	<li>All images must be stored in the images folder</li>
	<li>Use 4 CSS files:
		<ul>
			<li><a href="./styles/4-common.css">styles/4-common.css: </a>for global style(i.e. the body and .container styles)</li>
			<li><a href="./styles/3-header.css">styles/3-header.css: </a>for header style</li>
			<li><a href="./styles/3-footer.css">styles/3-footer.css: </a>for footer style</li>
			<li><a href="./styles/5-filters.css">styles/5-filters.css: </a>for filters style</li>
			<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
</ul>

## Task 6
* **It's (h)over**
[6-index.html](./6-index.html): HTML page that displays a header, footer and a filters box with a search button.
<h2>Layout</h2>
Based on <a href="./5-index.html">5-index.html</a>
<ul>
	<li> Update Locations and Amenities filters to displaty a contextual dropdown when the mouse is on the filter div:
		<ul>	
			<li>tag ul</li>
			<li>classname: popover</li>
			<li>text should be fake now/li>
			<li>inside each div</li>
			<li>not displayed by default</li>
			<li>color #FAFAFA</li>
			<li>width: same as the div filter</li>
			<li>border #DDDDDD 1px with border radius 4px</li>
			<li>no list display</li>
			<li>Location filter has 2 levels of ul/li:
				<ul>
					<li>state -> cities</li>
					<li>state name must be display in a h2 tag(font size 16px)</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<h3>Reuirements</h3>
<ul>
	<li>Use the: header, footer, section, button, h3, h4, ul, li tags</li>
	<li>No inline style</li>
	<li>img tag is not allowed</li>
	<li>Use of the style tag in the head tag not allowed</li>
	<li>All images must be stored in the images folder</li>
	<li>Use 4 CSS files:
		<ul>
			<li><a href="./styles/4-common.css">styles/4-common.css: </a>for global style(i.e. the body and .container styles)</li>
			<li><a href="./styles/3-header.css">styles/3-header.css: </a>for header style</li>
			<li><a href="./styles/3-footer.css">styles/3-footer.css: </a>for footer style</li>
			<li><a href="./styles/6-filters.css">styles/6-filters.css: </a>for filters style</li>
			<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
</ul>

## Task 7
* **Display results**
[7-index.html](./7-index.html): HTML page that displays a header, footer, a filters box with dropdown and results.
<h2>Layout</h2>
Based on <a href="./6-index.html">6-index.html</a>
<ul>
	<li>Add Places section:
		<ul>
			<li>tag section</li>
			<li>classname: places</li> 
			<li>same level as filters section, inside .containers</li>
			<li>contains title
				<ul>
					<li>tag: h1</li>
					<li>text: places</li>
					<li>align in the top left</li>
					<li>font size: 30px</li>
				</ul>
			</li>
			<li>contains multiple "Places" as listing (horizontal or vertical) describe by: 
				<ul>
					<li>tag: article</li>
					<li>width: 390px</li>
					<li>padding and margin 20px</li>
					<li>border #FF5A5F with radius 4px</li>
					<li>contains the place name:
						<ul>
							<li>tag h2</li>
							<li>font size: 30px</li>
							<li>center horizontally</li>
						</ul>		
					</li>
				</ul>
			</li>
		</ul>
	</li>
</ul>
<h3>Reuirements</h3>
<ul>
	<li>Use the: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags</li>
	<li>No inline style</li>
	<li>img tag is not allowed</li>
	<li>Use of the style tag in the head tag not allowed</li>
	<li>All images must be stored in the images folder</li>
	<li>Use 5 CSS files:
		<ul>
			<li><a href="./styles/4-common.css">styles/4-common.css: </a>for global style(i.e. the body and .container styles)</li>
			<li><a href="./styles/3-header.css">styles/3-header.css: </a>for header style</li>
			<li><a href="./styles/3-footer.css">styles/3-footer.css: </a>for footer style</li>
			<li><a href="./styles/6-filters.css">styles/6-filters.css: </a>for filters style</li>
			<li><a href="./styles/7-places.css">styles/7-places.css: </a>for places style</li>
			<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
</ul>

## Task 8
* **More details**
[8-index.html](.8-index.html): HTML page that displays a header, a footer, a filter box(dropdwon list) and the result of the search.
<h2>Layout</h2>
<p>Based on [7-index.html](./7-index.html)</p>
<p>Add more informaiton to a place article:</p>
<ul>
	<li>Price by night:
		<ul>
			<li>tag div</li>
			<li>classname: price_by_night</li>
			<li>same level as the place name</li>
			<li>font color: #FF5A5F</li>
			<li>border: #FF5A5F 4px rounded</li>
			<li>min width: 60px</li>
			<li>height: 60px</li>
			<li>font size: 30px</li>
			<li>align: the top right (with space)</li>
		</ul>
	</li>
	<li> Information section:
		<ul>
			<li>tag div</li>
			<li>classname: information</li>
			<li>height: 80px</li>
			<li>border: top and bottom #DDDDDD 1px</li>
			<li>contains (align vertically):
				<ul>
					<li>Number of guests:
						<ul>
							<li>tag div</li>
							<li>classname: max_guest</li>
							<li>width: 100px</li>
							<li>fake text</li>
							<li>icon</li>
						</ul>
					</li>
					<li>Number of bedrooms:
						<ul>
							<li>tag div</li>
							<li>classname: number_rooms</li>
							<li>width: 100px</li>
							<li>fake text</li>
							<li>icon</li>
						</ul>
					</li>
					<li>Number of bathrooms:
						<ul>
							<li>tag div</li>
							<li>classname: number_bathrooms</li>
							<li>width: 100px</li>
							<li>fake text</li>
							<li>icon</li>
						</ul>
					</li>
				</ul>
			</li>
		</ul>
	</li>
	<li> User section:
		<ul>	
			<li>tag div</li>
			<li>classname: user</li>
			<li>text Owner: <fake text></li>
			<li>Owner text should be in bold</li>
		</ul>
	</li>
	<li> Description section:
		<ul>	
			<li>tag div</li>
			<li>classname: description</li>
		</ul>
	</li>
</ul>
<h3>Reuirements</h3>
<ul>
	<li>Use the: header, footer, section, article, button, h1,, h2, h3, h4, h5, ul, li tags</li>
	<li>No inline style</li>
	<li>img tag is not allowed</li>
	<li>Use of the style tag in the head tag not allowed</li>
	<li>All images must be stored in the images folder</li>
	<li>Use 5 CSS files:
		<ul>
			<li><a href="./styles/4-common.css">styles/4-common.css: </a>for global style(i.e. the body and .container styles)</li>
			<li><a href="./styles/3-header.css">styles/3-header.css: </a>for the header style</li>
			<li><a href="./styles/3-footer.css">styles/3-footer.css: </a>for the footer style</li>
			<li><a href="./styles/6-filters.css">styles/6-filters.css: </a>for the filters style</li>
			<li><a href="./styles/8-places.css">styles/8-places.css: </a>for the places style</li>
			<li>Must be <a href="https://github.com/holbertonschool/W3C-Validator">W3C valid</a></li>
</ul>
