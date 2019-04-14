---
title: 传热学绪论
date: 2019-04-14 21:19:0
categories: 传热学
mathjax: true
---

# 热量传递的基本形式

|  形式  |                          备注                          |
| :----: | :----------------------------------------------------: |
| 热传导 | ![热传导](/assert/img/heat-transfer/intro-热传导.webp) |
| 热对流 | ![热对流](/assert/img/heat-transfer/intro-热对流.webp) |
| 热辐射 | ![热辐射](/assert/img/heat-transfer/intro-热辐射.webp) |

## 傅里叶定律(一维形式)

$$
q = \frac{\Phi}{A} = - \lambda \frac{\mathrm{d} t}{\mathrm{d}x}
$$

- $\lambda$ 是比例系数, 称为 "热导率" 或 "导热系数", 量纲为 $\dfrac{[M][L]}{[T][t]^3}$
- $\Phi$ 为通过界面的热量, 称作 "热流量", 量纲与功率相同.
- $q$ 为 "热流密度", 是通过单位面积的热流量

导热系数表征了材料的导热能力的大小.

### 稳态一维平板导热

![intro-一维平板传热](/assert/img/heat-transfer/intro-一维平板传热.webp)

对一维傅里叶定律进行积分, 得到

$$ q \mathrm{d} x = - \lambda \mathrm{d} t $$
$$ \int_0^\delta q \mathrm{d} x = \int_{t_1}^{t_2} -\lambda \mathrm{d} t $$
$$ q\delta = -\lambda \Delta t $$
$$ q=\frac{-\Delta t}{\frac{\delta}{\lambda}} $$

在形式上, 稳态一维平板导热和电路中的欧姆定律等同了起来:

$$ q=\frac{-\Delta t}{\frac{\delta}{\lambda}}  $$
$$ I = \frac{- \Delta V}{R} $$

- $q$ 热流密度和 $I$ 电流对应
- $-\Delta t$ 温度差和 $- \Delta V$ 电位差对应

则理所应当地, 推理出 $\frac{\delta}{\lambda}$ 与 $R$ 对应.

而在很多情况下, $\frac{\delta}{\lambda}$ 的确对计算起到了方便作用, 有一定的物理意义, 因此定义它为 "热阻".

## 牛顿冷却公式

牛顿冷却公式表示 "对流热交换中, 热量传递的效率与温差成正比"

$$ q=\frac{\Phi}{A} = - h \Delta t $$

- $A$ 表示两个物体相互接触的表面积
- $\Delta t$ 表示两个物体的温度差
- $h$ 是 "表面传热系数", 描述了 流速,流体物性,接触面形态 等影响传热效率的对象.

## 黑体辐射

"黑体" 是一个理想模型, 表示此物体不会反射任何辐射, 所有发出的辐射全部源于自身.
黑体向外辐射的热流量可用 Stefan-Boltzmann 定律计算:

$$ q = \frac{\Phi}{A} = \sigma T^4 $$

- $\sigma$ 为 Stefan-Boltzmann 常量, 是黑体辐射常数 `5.67e-8` $Wm^{-2}K^{-4}$

### 实际物体的热辐射

实际物体的热辐射可由黑体辐射概念继承而来, 引入一个 "发射率" 属性(又称 "黑度"), 数值在 `[0, 1]` 之间, 与物体的材质, 表面情况 有关.

$$ q = \frac{\Phi}{A} = \varepsilon \sigma T^4 $$

- $\varepsilon$ 为黑度.

实际物体的热辐射, 就是 黑体辐射 \* 黑度 进行修正.

# 小结

|                       公式                        | 含义                   |
| :-----------------------------------------------: | ---------------------- |
|   $$ q \mathrm{d} x = - \lambda \mathrm{d} t $$   | 一维情况下的傅里叶定律 |
| $$ q=\frac{-\Delta t}{\frac{\delta}{\lambda}} $$  | 一维稳态下的傅里叶定律 |
|       $$ q=\frac{\Phi}{A} = - h \Delta t $$       | 牛顿冷却公式           |
| $$ q = \frac{\Phi}{A} = \varepsilon \sigma T^4 $$ | 实际物体的热辐射       |
