import asyncio
import asyncio  
import time

async def brew(name):
  print(f"Brewing {name}...")
  # await asyncio.sleep(2)
  time.sleep(3)
  print(f"{name} is ready✅")

async def main():
  await asyncio.gather(
      brew("chai"),
  brew("coffee"),
  brew("tea")
  )

asyncio.run(main())