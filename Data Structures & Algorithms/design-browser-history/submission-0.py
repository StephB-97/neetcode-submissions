class Node:
    def __init__(self, url = None, left = None, right = None):
        self.url = url
        self.left = left
        self.right = right


class BrowserHistory:

    def __init__(self, homepage: str):
        self.base = Node(homepage)
        
        
        

    def visit(self, url: str) -> None:
        new_page = Node(url, self.base)
        self.base.right = new_page
        self.base = new_page

        
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.base.left == None:
                self.base = self.base
            else:
                self.base = self.base.left
       
        return self.base.url

            
        
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.base.right == None:
                self.base = self.base
            else:
                self.base = self.base.right
       
        return self.base.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)