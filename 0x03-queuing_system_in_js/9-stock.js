import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';


const app = express();
const client = createClient();

client.on('connect', () => console.log('Redis client connecte>

client.on('error', (err) => console.log(`Redis client not con>


const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];


function getItemById(id) {
  // Check if the given id exist in the listProduct
  // If so return the data.
  return listProducts.find((item) =>  item.id === id);
}

function reserveStockById(itemId, stock) {
  // Set the item id on the redis server
  client.set(`item.${itemId}`, stock, (err, reply) => {
    console.log(reply);
  });
}

async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock;
}

app.get('/list_products', (req, res) => {
  const responsePayload = listProducts.map((item) => {
    return {
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
    };
  });

  res.json(responsePayload);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const availableStock = item.stock - reservedStock;

    res.json({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity: availableStock,
    });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.status(404).json({ status: 'Product not found' });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const availableStock = item.stock - reservedStock;

    if (availableStock <= 0) {
      res.status(403).json({ status: 'Not enough stock available', itemId });
    }

    reserveStockById(itemId, Number(reservedStock) + 1);

    res.json({ status: 'Reservation confirmed', itemId });
  }
});

app.listen(1245);
