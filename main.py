import requests
import argparse

url = ''
data = {'room_id': '','csrf_token':'','csrf':'','area_v2':'','platform':'pc','backup_stream':0}
headers = {'accept': 'application/json, text/plain, */*','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36','content-type':'application/x-www-form-urlencoded;charset=UTF-8','cookie':''}

def main():
	parser = argparse.ArgumentParser(description='Send HTTP POST request with provided parameters.')

	parser.add_argument('--cookie', required=True, type=str, help='你的Cookie')
	parser.add_argument('--token', required=True, type=str, help='你的Token')
	parser.add_argument('--room_id', required=True, type=int, help='你的房间号')
	parser.add_argument('--area', required=True, type=int, help='分区')
	parser.add_argument('--startlive', action='store_true', help='开始直播')
	parser.add_argument('--stoplive', action='store_true', help='结束直播')

	args = parser.parse_args()

	if args.startlive == args.stoplive:
		parser.error('You must specify either --startlive or --stoplive, but not both or neither.')

	data['room_id']=args.room_id
	data['csrf']=args.token
	data['csrf_token']=args.token
	headers['cookie']=args.cookie
	data['area_v2']=args.area
	if(args.startlive):
		url = 'https://api.live.bilibili.com/room/v1/Room/startLive'
	elif(args.stoplive):
		url = 'https://api.live.bilibili.com/room/v1/Room/stopLive'
	response = requests.post(url,data=data,headers=headers)
	print(response.status_code)
	response_data=response.json()
	if(response_data['code']):
		print("Errer!\ncode:{}\nmessage:{}".format(response_data['code'],response_data['message']))
	else:
		if(args.startlive):
			rtmp=response_data['data']
			rtmp=rtmp['rtmp']
			print("rmtp:{}\nkey:{}".format(rtmp['addr'],rtmp['code']))
		elif(args.stoplive):
			print('Success.')

if __name__ == '__main__':
	main()