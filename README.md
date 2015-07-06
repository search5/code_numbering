# code_numbering

== Usage ==
기본 사용법
<code>
python number_tagging.py 텍스트파일 > number_tagging_filename or clipboard copy cmd
</code>

확장 사용법
<code>
python number_tagging.py 텍스트파일 시작줄번호-1 > number_tagging_filename or clipboard copy cmd
</code>

== 결과 ==
<pre>
01: __author__ = 'jiho'
02: 
03: import sys
04: 
05: def main(argv, start_num=0):
06:     src_file_line_count = bufcount(argv)
07: 
08:     src_file = open(argv, "r")
09:     out_file = None
</pre>
