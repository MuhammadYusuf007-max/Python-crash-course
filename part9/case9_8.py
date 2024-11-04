class Privilege:
    def __init__(self):
        self.privilege = ["can add post", "can delete post", "can ban user"]


    def show_privilege(self):
        print("admin can do this type works only")
        for i in self.privilege:
            print(f"\t-{i}")
            
Yusuf = Admin("Yusuf", "mukhammadov", "first time work this type work")
Yusuf.show_privilege()