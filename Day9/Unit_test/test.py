import unittest
import Msin
class Testcalc(unittest.TestCase):
    def test_add(Self):
        Self.assertEqual(Msin.add(10,5),15)
        Self.assertEqual(Msin.add(10,4),14)
        Self.assertEqual(Msin.add(10,2),12)
    def test_sub(Self):
        Self.assertEqual(Msin.sub(10,5),5)
        Self.assertEqual(Msin.sub(10,4),6)
        Self.assertEqual(Msin.sub(10,2),8)
    def test_mul(Self):
        Self.assertEqual(Msin.mul(10,5),50)
        Self.assertEqual(Msin.mul(10,4),40)
        Self.assertEqual(Msin.mul(10,2),20)
    def test_di(Self):
        Self.assertEqual(Msin.div(10,2),5)
        Self.assertEqual(Msin.div(8,4),2)
        Self.assertEqual(Msin.div(20,2),10)
        Self.assertRaises(ValueError,Msin.div,10,0)
    def test_com(Self):
        first=4
        second=4
        message="It is failed"
        Self.assertLessEqual(first,second,message)
    def test_nq(Self):
        first="Kavi"
        second="Kavi"
        #second="Kaviarasu"
        message="It is failed"
        Self.assertEqual(first,second,message)
    def test_check(Self):
        testcase=True
        Self.assertTrue(testcase,"It is not true")
    def test_check1(Self):
        testcase=False
        Self.assertFalse(testcase,"It is not true")
if __name__=='__main__':
    unittest.main()
