import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
OUT=Path.home()/"rpa-course/ads/out"; OUT.mkdir(parents=True,exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1120,"height":1120},device_scale_factor=1)
        await pg.goto("file://"+str(Path.home()/"rpa-course/ads/ads.html"))
        await pg.wait_for_timeout(500)
        for i in range(1,13):
            await pg.locator(f"#c{i}").screenshot(path=str(OUT/f"ad{i}.png"))
        await b.close()
    print("CARDS_DONE 12")
asyncio.run(main())
