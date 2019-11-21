extends Node2D

var headers = ["Content-Type: application/json"]
var url = "http://localhost:8000/api/"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button_pressed():
	var username = $TextUsuario.text
	var password = $LineEditSenha.text
	var data = {"username":username, "password":password}
	var query = JSON.print(data)
	$HTTPRequest.request(url+"logado/",headers, false, HTTPClient.METHOD_POST,query)


func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	if result == HTTPRequest.RESULT_SUCCESS:
		if response_code == 200:
			var dados = JSON.parse(body.get_string_from_utf8())
			headers.append("Authorization: token "+dados.result.token)
			$HTTPGetAvatar.request(url+"avatar/?owner="+str(dados.result.id),headers, false, HTTPClient.METHOD_GET,"")
		else:
			print("fail")


func _on_ButtonSair_pressed():
	get_tree().quit()


func _on_HTTPGetAvatar_request_completed(result, response_code, headers, body):
	if result == HTTPRequest.RESULT_SUCCESS:
		if response_code == 200:
			var dados = JSON.parse(body.get_string_from_utf8())
			Global.owner_id = dados.result[0].owner
			Global.avatarName = dados.result[0].name
			Global.force = dados.result[0].force
			Global.defence = dados.result[0].defense
			Global.life = dados.result[0].life
			Global.level = dados.result[0].level
			Global.knowings = dados.result[0].knowing
			Global.itens = dados.result[0].item
			print(Global.itens)
			print(Global.knowings)
			get_tree().change_scene("res://Senas/FaseUm.tscn")