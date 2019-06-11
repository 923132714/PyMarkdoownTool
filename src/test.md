---
data : 2018/ 2/ 26
export_on_save : 
  html : false
html :
  embed_local_images : true
  embed_svg : true
  offline : true
  toc : undefined
print_background : false
updated : 2018/ 2/ 26
---

**邮箱** liuling@bjut.edu.cn
**教师** 刘玲
# 随机事件

<span id = "基本概念"></span>
## &nbsp;基本概念

<span id = "随机试验"></span>
### &emsp;随机试验

一次观察、观测称为试验。试验在相同下条件下可 **重复** 进行，每次 **不可预知** ，称`试验`，用 $E$ 表示。

### &emsp;样本空间

**所有** 可能结果集合用 $Ω$ 表示。

### &emsp;样本空间元素

**单个** 可能结果，用 $ω$ 表示。

### &emsp;随机事件
样本空间的任意一个 **子集** ，使用 $A $ $B$ $C$ 表示。
当ω属于A，称A`发生`。
如果事件中只含有一个试验结果(样本空间中的一个元素)，该事件称`基本事件`，否则为`复合事件`。

<span id = "随机事件的特点"></span>
## &nbsp;事件的特点

单次 **不可预知**，**范围已知**
具有`统计规律性`
<span id = "事件的关系与运算"></span>
## &nbsp;事件的关系

### &emsp;包含

若A发生B一定发生记为，则事件A包含于事件B，记为$A\subseteq B$
若A包含于B，B包含于A，则  $A=B$

### &emsp;和或并

若C发生当且仅当A或B发生，记为 $C=A\bigcup B$
若C发生当且仅当$A_0$~$A_n$发生，记为$C = \bigcup_{i=0}^n A_i$



### &emsp;交或积
若C发生当且仅当AB同时发生，记为$C=AB$或$C=A\bigcap B$
若C发生当且仅当$A_0$~$A_n$同时发生，记为![交或积]( http://latex.codecogs.com/gif.latex?C=\bigcap_{i=0}^nA_i)

### &emsp;互斥
AB不可能同时发生，记为$AB=\emptyset$

### &emsp;差
A与B的差，当A发生切B不发生，记为$C=A-B$

### &emsp;逆或补
A的逆 表示A不发生，记为 $\overline A$

<span id = "运算法则"></span>
## &nbsp;运算法则
### &emsp;交换律
$A\bigcup B =B\bigcup A$

$AB =BA$
### &emsp;结合律
$A\bigcup (B\bigcup C) =(A\bigcup B)\bigcup C$

$A(BC) =(AB)C$

### &emsp;分配率
$A\bigcap (B\bigcup C) =(AB)\bigcup (AC)$

$A\bigcup (B C) =(A\bigcup B) (A\bigcup C)$

### &emsp;对偶率

$\overline {A\bigcup B} = \overline A \bigcap \overline B$

$\overline {A B} = \overline A \bigcup \overline B$
### &emsp;其他

$A-B = A\overline B$

$A = (AB)\bigcup(A\overline B)$