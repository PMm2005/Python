class Player:
    def __init__(self, name, age, position, team):
        self.name = ['name']
        self.age = ['age']
        self.position = ['position']
        self.team = ['team']

kevin = {
    "name": "Kevin Durant", 
	"age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
}
jason = {
	"name": "Jason Tatum", 
	"age":24, 
	"position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
	"name": "Kyrie Irving", 
	"age":32,
    "position": "Point Guard", 
	"team": "Brooklyn Nets"
}

kevin = Player(name="Kevin Durant", age=34, position="small forward", team="Brooklyn Nets")
jason = Player(name="Jason Tatum", age=24, position="small forward", team="Boston Celtics")
kyrie = Player(name="Kyrie Irving", age=32, position="Point Guard", team="Brooklyn Nets")

