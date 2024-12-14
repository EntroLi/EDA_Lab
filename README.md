# Lab3

## run log

~~~bash
Dir: 001 with ADP: 4429775.547648 // random
Dir: 002 with ADP: 3312383.1552 // random
Dir: 003 with ADP: 2695614.9325056 // sklansky + wallace + None Seed
Dir: 004 with ADP: 2695614.9325056 // sklansky + wallace + None Seed
Dir: 005 with ADP: 2607057.8030592 // sklansky + dadda + None Seed
Dir: 006 with ADP: 2989924.897536 // koggestone + wallace + None Seed
Dir: 007 with ADP: 2463628.898304 // koggestone + dadda + None Seed
Dir: 008 with ADP: 2944948.6089215996 // brentkung + wallace + None Seed
Dir: 009 with ADP: 2614895.364096 // brentkung + dadda + None Seed
Dir: 010 with ADP: 2456811.399168 // default try1 + dadda + None Seed
Dir: 011 with ADP: 1203994.5463295998 // clk=0.5 uti=0.7
~~~

## Baseline

1. 全随机 允许违例
2. 全随机 统计不为例的比例 不允许违例

统计代码

1. try1 + dadda 对工具随机，允许违例、
2. try1 + dadda 对工具随机，统计不为例的比例 不允许违例

统计代码，比较Try1的提升



@qxh

先手动调参：clk+eff 0.2*0.98

其他参数的定性影响（半定量，影响大吗？）ADP是核心指标

@cwc+lsy

test 0.1 0-99

run 0.2 0.98 for[Sklansky Koggestone Brentkung Try1] [Wallace Dadda] 



Best Dir

0.2 0.98 74.9w
