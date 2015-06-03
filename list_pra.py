import sys

def main():
	productList = ["fruit:100","clothes:1000","vegetale:300","rice:20"]
	salary = int(raw_input("please input your salary: "))
	while True:
		print "product list:\n"
		i = 0
		for product in productList:
			print "%d,%s" %(i,product)
			i +=1
		chooses = raw_input("please input you chooses:(splist by ',')")
		spend = 0
		chooseproduct = []
		for index in chooses.split(","):
			chooseproduct.append(productList[index].split(":")[0])
			spend += productList[index].split(":")[1]
		print "you spend %d" % spend
		left = salary - spend
		if left <= 0:
			print "your money is not enough"
			sys.exit(0)
		else:
			print "your product list :",chooseproduct

if __name__ == '__main__':
	main()