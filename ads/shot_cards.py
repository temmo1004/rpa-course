import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
OUT=Path.home()/"rpa-course/ads/out"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1120,"height":1120},device_scale_factor=1)
        await pg.goto("file://"+str(Path.home()/"rpa-course/ads/ads.html"))
        await pg.wait_for_timeout(600)
        for i in range(1,15):
            await pg.locator(f"#c{i}").screenshot(path=str(OUT/f"ad{i}.png"))
        await b.close()
    print("DONE 14")
asyncio.run(main())
