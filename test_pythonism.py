import pytest

from pythonism import MyNewCollection

def test_for_in():

    collection = MyNewCollection(("TestOne","TestTwo","TestThree"))

    collection_list = []

    for collection in collection:
        collection_list.append(collection)

    assert collection_list == ["TestOne","TestTwo","TestThree"]


# @pytest.mark.skip("pending")
def test_list_comprehension():

    collection = MyNewCollection(("TestOne","TestTwo","TestThree"))

    cap_collections = [collection.upper() for collection in collection]

    assert cap_collections == ["TESTONE","TESTTWO","TESTTHREE"]

# @pytest.mark.skip("pending")
def test_list_cast():

    collection_list = ["TestOne","TestTwo","TestThree"]

    collections = MyNewCollection(collection_list)

    assert list(collections) == collection_list


# @pytest.mark.skip("pending")
def test_range():

    num_range = range(1,20+1)

    nums = MyNewCollection(num_range)

    assert len(nums) == 20



# @pytest.mark.skip("pending")
def test_filter():

    nums = MyNewCollection(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]


# @pytest.mark.skip("pending")
def test_next():

    collections = MyNewCollection(["TestOne","TestTwo","TestThree"])

    iterator = iter(collections)

    assert next(iterator) == "TestOne"
    assert next(iterator) == "TestTwo"
    assert next(iterator) == "TestThree"


# @pytest.mark.skip("pending")
def test_stop_iteration():

    collections = MyNewCollection(["TestOne","TestTwo","TestThree"])

    iterator = iter(collections)

    with pytest.raises(StopIteration):
        while True:
            collection = next(iterator)

# @pytest.mark.skip("pending")
def test_str():
    collections = MyNewCollection(["TestOne","TestTwo","TestThree"])
    assert str(collections) == "[ TestOne ] -> [ TestTwo ] -> [ TestThree ] -> None"

# dunder method tests

# @pytest.mark.skip("pending")
def test_equals():

    lla = MyNewCollection(["TestOne","TestTwo","TestThree"])
    llb = MyNewCollection(["TestOne","TestTwo","TestThree"])

    assert lla == llb

# @pytest.mark.skip("pending")
def test_get_item():

    collections = MyNewCollection(["apple","banana","cucumber"])

    assert collections[0] == "apple"

# @pytest.mark.skip("pending")
def test_get_item_out_of_range():

    collections = MyNewCollection(["apple","banana","cucumber"])

    with pytest.raises(IndexError):
        collections[100]