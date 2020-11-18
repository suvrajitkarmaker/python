class BinarySearch:
    def __init__(self, list_of_item):
        self.list_of_item = list_of_item
        self.length = len(list_of_item)
        
    def search(self, value):
        lo=0
        high = self.length
        while(lo<=high):
            mid = lo + (high - lo) // 2
            if(self.list_of_item[mid] == value):
                return True
            elif(value > self.list_of_item[mid]):
                lo = mid + 1
            else:
                high = mid - 1
        return False
    
    def lowerBound(self, value):
        lo=0
        high = self.length
        while(lo < high):
            mid = lo + (high - lo) // 2
            if(value <= self.list_of_item[mid]):
                high = mid
            else:
                lo = mid + 1
        return lo
    
    def upperBound(self, value):
        lo=0
        high = self.length
        while(lo < high):
            mid = lo + (high - lo) // 2
            if(value >= self.list_of_item[mid]):
                lo = mid + 1
            else:
                high = mid
        return lo


list = [10, 15, 16, 16, 19, 25, 25, 28, 28]

bs = BinarySearch(list)
print(bs.search(25))
print(bs.lowerBound(17))
print(bs.upperBound(25))