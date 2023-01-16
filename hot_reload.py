import asyncio
import keyboard
from playwright.async_api import Playwright, async_playwright

async def run(playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto('http://localhost:3000/index.php')
    while True:
      keyboard.wait('alt')
      print('reloading..')
      await page.reload()

async def main():
  async with async_playwright() as playwright:
    await run(playwright)


asyncio.run(main())
