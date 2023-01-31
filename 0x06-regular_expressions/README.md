<img src="https://bennadel-cdn.com/resources/uploads/2022/i-see-patterns-theyre-everywhere.jpg">

# Regular Expressions



Regular expressions (Regex) are a powerful tool used to match patterns of text. Regex can be used to identify and manipulate text, such as searching for a specific string, replacing text, and validating input.



## Syntax



Regex consists of a series of characters that define a search pattern. The syntax used to define patterns can vary depending on the language or tool being used, but most regex is written in a language called **POSIX Extended Regular Expressions**.



## Usage



Regex is used in a variety of tools and programming languages, including JavaScript, Ruby, and Python. The most common use of regex is for string manipulation and data validation, such as validating email addresses, phone numbers, and URLs. Regex is also used for text search and replace operations, and can be used to extract data from a string.

## Getting Started



To use regular expressions in Ruby, you'll need to import the Regexp class. The most common way is to include the following line at the top of your script:



```ruby

require 'regexp'

```



## Syntax



Regular expression syntax is denoted by forward slashes `/` surrounding a pattern of characters. For example:



```ruby

/\d{3}-\d{3}-\d{4}/

```



This pattern will match strings like `123-456-7890`. 



## Examples



Suppose you have a string of words and you want to find all the four-letter words in it. You could use the following pattern:



```ruby

/\b\w{4}\b/

```



Or maybe you have a list of URLs and you want to extract the domain name from each one. You could use this pattern:



```ruby

/https?:\/\/(?:www\.)?(.+?)\//

```

## Jokes
Q: What did the regex say to its date?

A: "You're so pattern-alicious!"
