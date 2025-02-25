
<p align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://raw.githubusercontent.com/KissmeBro/aioengine/refs/heads/main/theme_dark.png" alt="Dark Theme" style="width: 140px; height: auto;">
        <br>Dark Theme
      </td>
      <td align="center">
        <img src="https://raw.githubusercontent.com/KissmeBro/aioengine/refs/heads/main/theme_light.png" alt="Light Theme" style="width: 140px; height: auto;">
        <br>Light Theme
      </td>
    </tr>
  </table>
</p>

# aioengine  

> An asynchronous library for using search engines in Python.  

## ⭐ Features  
- ✅ **Asynchronous**  
- 🚀 **Simple**  
- 📈 **Scalable**  

---

## 📌 Examples  

### 🔹 Example 1  
```python
import asyncio
from aioengine import GoogleEngine, EngineError

async def main():
    api_key = "ABCDEFGHIJKLMNOP"
    cse_id = "1234567890"
    engine = GoogleEngine(api_key, cse_id)
    
    try:
        query = "python"
        results = await engine.search(query, num=5)
        for result in results:
            print(result.link)

    except EngineError as error:
        error.display_error()
        
if __name__ == "__main__":
    asyncio.run(main())
```
📂 **Directory:** [example_google_1.py](https://github.com/KissmeBro/aioengine/blob/main/examples/example_google_1.py)  

<br>

### 🔹 Example 2  
```python
import asyncio
from aioengine import GoogleEngine, EngineError

async def main():
    api_key = "ABCDEFGHIJKLMNOP"
    cse_id = "1234567890"
    
    async with GoogleEngine(api_key, cse_id) as engine:
        try:
            query = "python"
            results = await engine.search(query, num=5)
            for result in results:
                print(result.link)

        except EngineError as error:
            error.display_error()

if __name__ == "__main__":
    asyncio.run(main())
```
📂 **Directory:** [example_google_2.py](https://github.com/KissmeBro/aioengine/blob/main/examples/example_google_2.py)  

<br>

---

## 📂 Project Structure  
- [`aioengine/`](https://github.com/KissmeBro/aioengine/blob/main/aioengine)
  - [`__init__.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/__init__.py)
  - `engines/`
    - [`__init__.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/engines/__init__.py)
    - [`google/`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/engines/google)
      - [`__init__.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/engines/google/__init__.py)
      - [`google.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/engines/google/google.py)
      - [`network.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/engines/google/network.py)
      - [`parser.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/engines/google/parser.py)
  - [`exceptions.py`](https://github.com/KissmeBro/aioengine/blob/main/aioengine/exceptions.py)  

--- 
