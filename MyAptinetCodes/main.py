from Repositories.productRepository import ProductRepository
from services.dal import DAL


if __name__ == '__main__':
    dal = DAL()
    pr = ProductRepository(dal)
    # res = pr.getProduct("124")
    # print(res)
    # print(res.getName())
    # pr.updateWeightFeatures("123",16,3.4,8.5)
    # pr.InsertNewRow("125","cake",12,10,"desc for cake")
    # pr.updateProduct("126", "soap", 1.5, 1.4, "False", "False")
    # offer_list = pr.getOfferList()
    # print(offer_list)
    # print(pr.getSuggestionsOfProduct("123"))
    print(pr.insertIntoFactor("124"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
