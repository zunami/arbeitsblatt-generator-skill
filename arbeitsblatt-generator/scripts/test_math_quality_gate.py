import json
import subprocess
import sys
import tempfile
from pathlib import Path

script = Path(__file__).with_name('math_quality_gate.py')

def run(tasks):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / 'tasks.json'
        p.write_text(json.dumps(tasks), encoding='utf-8')
        result = subprocess.run([sys.executable, str(script), str(p)], capture_output=True, text=True)
        return result.returncode, json.loads(result.stdout)

valid = [
    {'id':'a','type':'operation','a':123,'b':77,'operator':'+','answer':200},
    {'id':'b','type':'division_remainder','dividend':29,'divisor':5,'quotient':5,'remainder':4},
    {'id':'c','type':'sequence_arithmetic','terms':[3,7,11,15],'next':19},
    {'id':'d','type':'rectangle','width':4,'height':6,'metric':'perimeter','answer':20},
    {'id':'e','type':'operation','a':'0.1','b':'0.2','operator':'+','answer':'0.3'},
]
code, out = run(valid)
assert code == 0 and all(x['ok'] for x in out), out
code, out = run(valid + [{'id':'bad','type':'operation','a':3,'b':4,'operator':'*','answer':13}])
assert code == 1 and out[-1]['ok'] is False, out
code, out = run([{'id':'zero','type':'operation','a':3,'b':0,'operator':'/','answer':0}])
assert code == 1 and 'division by zero' in out[0]['error'], out

advanced = [
    {'id':'alternate','type':'sequence_alternating','terms':[5100,4900,5300,5100],
     'steps':[-200,400],'continuation':[5500,5300,5700],'min_value':0,'max_value':10000},
    {'id':'neighbor','type':'neighbors','number':3927,'base':100,'lower':3900,'upper':4000},
    {'id':'edge','type':'neighbors','number':10000,'base':100,'lower':9900,'upper':10100},
    {'id':'order','type':'order_numbers','numbers':[4901,4190,4910,4019],
     'direction':'ascending','answer':[4019,4190,4901,4910]},
    {'id':'chain','type':'consecutive_chain','anchor':4930,'step':1,'left_count':2,
     'right_count':3,'left':[4928,4929],'right':[4931,4932,4933]},
    {'id':'place','type':'place_value','places':{'E':2,'H':6,'T':4,'Z':8},
     'display_order':['E','H','T','Z'],'answer':4682},
    {'id':'digits','type':'digit_rearrangement','digits':[4,1,5,3],
     'operator':'-','largest':5431,'original':4153,'answer':1278},
    {'id':'step','type':'step_value','start':9960,'step':100,'direction':'add','answer':10060},
]
code, out = run(advanced)
assert code == 0 and all(x['ok'] for x in out), out
invalid = [
    {'id':'wrong_pattern','type':'sequence_alternating','terms':[5100,4900,5300,5100],
     'continuation':[5500,5400]},
    {'id':'false_neighbor','type':'neighbors','number':3927,'base':100,
     'lower':3827,'upper':4027},
    {'id':'false_edge','type':'neighbors','number':10000,'base':100,
     'lower':9900,'upper':11000},
    {'id':'lost_number','type':'order_numbers','numbers':[1234,2345,3456],
     'direction':'ascending','answer':[1234,2345,2345]},
    {'id':'false_chain','type':'consecutive_chain','anchor':4930,'left_count':2,
     'right_count':1,'left':[4927,4929],'right':[4931]},
    {'id':'false_place','type':'place_value','places':{'E':2,'H':6,'T':4,'Z':8},
     'answer':4862},
    {'id':'wrong_digits','type':'digit_rearrangement','digits':[4,1,5,3],
     'operator':'-','largest':5431,'original':4315,'answer':1116},
    {'id':'wrong_step','type':'step_value','start':9960,'step':100,
     'direction':'add','answer':9970},
]
code, out = run(invalid)
assert code == 1 and len(out) == len(invalid) and all(not x['ok'] for x in out), out
written_ok = {'id':'written','type':'division_written','dividend':5628,
    'divisor':5,'quotient':1125,'remainder':3,'steps':[
    {'partial':5,'quotient_digit':1,'subtracted':5,'remainder':0},
    {'partial':6,'quotient_digit':1,'subtracted':5,'remainder':1},
    {'partial':12,'quotient_digit':2,'subtracted':10,'remainder':2},
    {'partial':28,'quotient_digit':5,'subtracted':25,'remainder':3}]}
code,out=run([written_ok])
assert code==0 and out[0]['ok'],out
wrong_written = dict(written_ok)
wrong_written['steps'] = [dict(x) for x in written_ok['steps']]
wrong_written['steps'][2]['subtracted'] = 11
code,out=run([wrong_written])
assert code==1 and not out[0]['ok'],out
# A zero in the middle of a quotient must remain a distinct division step.
zero_quotient = {'id':'zero_step','type':'division_written','dividend':5020,
    'divisor':5,'quotient':1004,'remainder':0,'steps':[
    {'partial':5,'quotient_digit':1,'subtracted':5,'remainder':0},
    {'partial':0,'quotient_digit':0,'subtracted':0,'remainder':0},
    {'partial':2,'quotient_digit':0,'subtracted':0,'remainder':2},
    {'partial':20,'quotient_digit':4,'subtracted':20,'remainder':0}]}
code,out=run([zero_quotient])
assert code==0 and out[0]['ok'],out
print('3 original and 3 advanced test groups passed')


