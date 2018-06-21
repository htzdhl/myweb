# -*- coding: utf-8 -*-
import redis
conn = redis.StrictRedis()

###lua脚本载入程序###
def script_load(script):
	sha = [None]
	def call(conn,keys=[],args=[]):
		if not sha[0]:
			sha[0] = conn.execute_command("SCRIPT","LOAD",script,parse="LOAD")
		try:
			return conn.execute_command("EVALSHA",sha[0],len(keys),*(keys+args))
		except redis.exceptions.ResponseError as msg:
			if not msg.args[0].startswith("NOSCRIPT"):
				raise
	return call
	
###lua登录脚本###
login_lua = """
	if not redis.call("exists",KEYS[1]) then
		return false
	end
	local password = redis.call("hget",KEYS[1],"password")
	if not password == ARGV[1] then
		return false
	end
	return true
"""