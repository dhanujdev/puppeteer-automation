#!/usr/bin/env python3
import asyncio
from pyppeteer import launch

async def take_screenshot():
    # Launch the browser
    browser = await launch(headless=True)
    
    # Open a new page
    page = await browser.newPage()
    
    # Navigate to a website
    await page.goto('https://www.example.com')
    
    # Set viewport dimensions
    await page.setViewport({'width': 1280, 'height': 800})
    
    # Take a screenshot
    await page.screenshot({'path': 'example.png'})
    
    # Close the browser
    await browser.close()
    
    print("Screenshot saved as example.png")

# Run the async function
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(take_screenshot())