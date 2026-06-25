import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
OUT=Path.home()/"rpa-course/ads/face_out"; OUT.mkdir(parents=True,exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={"width":1120,"height":1120},device_scale_factor=1)
        await pg.goto("file://"+str(Path.home()/"rpa-course/ads/face.html"))
        await pg.wait_for_timeout(600)
        for i in range(1,5):
            await pg.locator(f"#f{i}").screenshot(path=str(OUT/f"face{i}.png"))
        await b.close()
    print("DONE")
asyncio.run(main())
