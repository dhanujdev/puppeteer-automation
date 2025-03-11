#!/usr/bin/env python3
import asyncio
from pyppeteer import launch

async def automate_form():
    # Launch the browser
    browser = await launch(headless=False)  # Set to True for headless mode
    
    # Open a new page
    page = await browser.newPage()
    
    # Navigate to a website with a form
    await page.goto('https://httpbin.org/forms/post')
    
    # Fill out form fields
    await page.type('input[name="custname"]', 'Test User')
    await page.type('input[name="custtel"]', '555-1234')
    await page.type('input[name="custemail"]', 'test@example.com')
    
    # Select a radio button
    await page.click('input[value="Medium"]')
    
    # Check a checkbox
    await page.click('input[name="topping"][value="bacon"]')
    
    # Select from dropdown
    await page.select('select[name="delivery"]', '1800')
    
    # Add a comment
    await page.type('textarea[name="comments"]', 'This is an automated test using Puppeteer')
    
    # Take a screenshot before submission
    await page.screenshot({'path': 'before_submit.png'})
    
    # Submit the form
    await page.click('button[type="submit"]')
    
    # Wait for navigation to complete
    await page.waitForNavigation()
    
    # Take a screenshot after submission
    await page.screenshot({'path': 'after_submit.png'})
    
    # Get the response text
    content = await page.content()
    print("Form submitted successfully!")
    
    # Close the browser
    await browser.close()

# Run the async function
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(automate_form())