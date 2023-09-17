defmodule Cart do
  def add(cart, item) do
    cart ++ [{:add, item}]
  end
end

ExUnit.start
defmodule CartTest do
  use ExUnit.Case
  test "adding to cart" do
    assert [{:add, 'item'}] == Cart.add [], 'item'
  end
end
