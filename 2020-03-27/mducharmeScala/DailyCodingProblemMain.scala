// author: mikaeld

object DailyCodingProblemMain {
  def main(args: Array[String]): Unit = {
    val in_1 = Seq(3,4,-1,1)
    val in_2 = Seq(1,2,0)
    val in_3 = Seq(1,1,-1,3,5,6,7,10,3)
    val in_4 = Seq(-1,-2,-3)
    val in_5 = Seq(-1,-2,-3,0)

    assert(lowest_positive_integer(in_1) == 2)
    assert(lowest_positive_integer(in_2) == 3)
    assert(lowest_positive_integer(in_3) == 2)
    assert(lowest_positive_integer(in_4) == 0)
    assert(lowest_positive_integer(in_5) == 1)

  }

  def lowest_positive_integer(array: Seq[Int]): Int = {
    val asSet = array.toSet
    val positiveOnly = for (i <- asSet if i >= 0) yield i

    if (positiveOnly.isEmpty)
      return 0

    val linearArray = (positiveOnly.min to positiveOnly.max + 1).toSet

    val difference = linearArray.diff(positiveOnly)

    if (difference.nonEmpty)
      return difference.min

    positiveOnly.max + 1
  }
}
