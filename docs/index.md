# 

<a href="https://socialify.git.ci">
    <img src="img/aiotieba.svg">
</a>

</p>

<div align="center">
<p>
<a href="https://github.com/Starry-OvO/aiotieba/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Starry-OvO/aiotieba/CI.yml?branch=develop&label=CI&logo=github&style=flat-square" alt="GitHub Workflow Status">
</a>
<a href="https://pypi.org/project/aiotieba">
    <img src="https://img.shields.io/pypi/v/aiotieba?color=g&style=flat-square" alt="PyPI - Version">
</a>
<a href="https://pypi.org/project/aiotieba">
    <img src="https://img.shields.io/pypi/pyversions/aiotieba?style=flat-square" alt="PyPI - Python Version">
</a>
</p>
</div>

---

## 简介

**aiotieba**使用[**aiohttp**](https://github.com/aio-libs/aiohttp)封装了大量[百度贴吧核心API](https://github.com/Starry-OvO/aiotieba/blob/master/aiotieba/client)

本框架以提高二次开发速度为首要设计目标，命名规则统一，类型注解和方法注释完全覆盖所有用户接口

## 安装并使用

+ 安装

```shell
pip install aiotieba
```

+ 体验一下

```python
import asyncio

import aiotieba


async def main():
    async with aiotieba.Client() as client:
        print(await client.get_threads("天堂鸡汤"))


asyncio.run(main())
```

+ 继续阅读[**入门教程**](tutorial/start.md)