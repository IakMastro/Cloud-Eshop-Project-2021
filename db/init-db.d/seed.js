db.developers.drop();
db.developers.insertMany([
    {_id: "609e4ed023333b00071a324d", name: "Kojima Productions"},
    {_id: "609e4f4e23333b00071a324f", name: "Ryu Ga Gotoku Studios"},
    {_id: "609e505623333b00071a3251", name: "Infinity Ward"},
    {_id: "609e529a23333b00071a3253", name: "Atlus"}
]);

db.genres.drop();
db.genres.insertMany([
    {_id: "609e566423333b00071a3255", name: "SA"},
    {_id: "609e567823333b00071a3257", name: "RPG"},
    {_id: "609e568923333b00071a3259", name: "FPS"}
]);

db.publishers.drop();
db.publishers.insertMany([
    {_id: "609e56b723333b00071a325b", name: "KONAMI"},
    {_id: "609e56ca23333b00071a325d", name: "SEGA"},
    {_id: "609e56df23333b00071a325f", name: "Activision"}
]);

db.games.drop();
db.games.insertMany([
    {
        _id: "609e575f23333b00071a3261",
        title: "Metal Gear Solid 3: Snake Eater",
        developer: "609e4ed023333b00071a324d",
        publisher: "609e56b723333b00071a325b",
        genre: "609e566423333b00071a3255"
    },
    {
        _id: "609e593323333b00071a3263",
        title: "Yakuza 0",
        developer: "609e4f4e23333b00071a324f",
        publisher: "609e56ca23333b00071a325d",
        genre: "609e567823333b00071a3257"
    },
    {
        _id: "609e59ca23333b00071a3265",
        title: "Call of Duty: Modern Warfare (2019)",
        developer: "609e505623333b00071a3251",
        publisher: "609e56df23333b00071a325f",
        genre: "609e568923333b00071a3259"
    },
    {
        _id: "609e5a2623333b00071a3267",
        title: "Persona 4: Golden",
        developer: "609e529a23333b00071a3253",
        publisher: "609e56ca23333b00071a325d",
        genre: "609e567823333b00071a3257"
    }
]);

db.users.drop();
db.users.insertMany([
    {
        _id: "609e5b9123333b00071a3269",
        username: "admin",
        password: "pass",
        admin: true,
        games_owned: {}
    },
    {
        _id: "609e5bc323333b00071a326b",
        username: "foo",
        password: "bar",
        admin: false,
        games_owned: {}
    }
]);