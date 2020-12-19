

### Strategy
  - ```unittest``` module, for both backend and frontend functionality.
  - ```Selenium WebDriver```
    - There could be used different webdriver to browser automation.
      - [Chrome](https://chromedriver.chromium.org/)
      - [Mozilla](https://github.com/mozilla/geckodriver/releases)
      
    - Due to highly usage of ```chromedriver```, I decided to benefit from Chrom environment. It is also a little bit faster than Mozilla.
  - Because of that the latest supported version to Arch of chromedriver, I have to use older version which is:
    - ```ChromeDriver 87.0.4280.88```


#### Why both ```Selenium``` and ```unittest``` exist at the same time ?
  - ```Selenium``` is required for the browser automations and client simulation.
  - ```unittest``` is required for testing each functionality, those are defined in our ```Jira``` project page.


### In Progress
  - [x] urls buttons click responses (```frontend```)
  - [ ] database highlevel viewing (```database```)
  - [ ] response time handling


#### Test Request

