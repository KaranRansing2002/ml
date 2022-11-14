{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "6baa73bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "aed8cc02",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r'Downloads/archive/uber.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "95e75a2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df.drop(['Unnamed: 0','key'],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "b814bd9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.dropna(axis=0,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "429f2f61",
   "metadata": {},
   "outputs": [],
   "source": [
    "def distance(lon1,lon2,lat1,lat2):\n",
    "    lon1,lon2,lat1,lat2 = map(np.radians,[lon1,lon2,lat1,lat2])\n",
    "    diff_lon=lon2-lon1\n",
    "    diff_lat=lat2-lat1\n",
    "    x=np.sin(diff_lat/2)**2\n",
    "    y=np.sin(diff_lon/2)**2\n",
    "    dist = 2*6371*np.arcsin(np.sqrt(x+np.cos(lat1)*np.cos(lat2)*y))\n",
    "    return dist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "b85127d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['distance']=distance(df['pickup_longitude'],df['dropoff_longitude'],df['pickup_latitude'],df['dropoff_latitude'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "b7567054",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2070d73c280>"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "mlp.scatter(df['distance'],df['fare_amount'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "abc1a18c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(df[df['fare_amount']<=0].index,inplace=True)\n",
    "df.drop(df[df['distance']<=0].index,inplace=True)\n",
    "df.drop(df[df['distance']>60].index,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "3af7020f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x20776599720>"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD4CAYAAAAXUaZHAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAAe2ElEQVR4nO3df4wc5Z3n8ffX4zaMSZYxMGvBGMfsBhmxIrGTOeLI0SnABhOIgo9kSXLJxbdC5z+OPwLLedecogSfEuHIuiVZ3SkSG6J1Liw7BMhgAlqDsKPdi2SWccYOMeDDYQHTEOwFDwl4gPb4e3909binp39UdVf/qKc/L8lyd3XP9FPdPZ966vlV5u6IiEhYFnS7ACIikj6Fu4hIgBTuIiIBUriLiARI4S4iEqCF3S4AwDnnnOMrVqzodjFERDJl7969/+buw9Ue64lwX7FiBRMTE90uhohIppjZi7UeU7OMiEiAFO4iIgFSuIuIBEjhLiISIIW7iEiAYo2WMbMXgN8DM8AJdx81s7OAMWAF8AJwvbsfMzMDvgdcDRwH/rO7/zLtgo9P5tm28yCvTE1z3tAgm9atZP3qkbRfRkQkk5LU3C9z91XuPhrd3ww87u4XAo9H9wE+DVwY/dsIfD+twpaMT+a59YGnyE9N40B+appbH3iK8cl82i8lIpJJrTTLXAtsj25vB9aXbf+RF+0Bhszs3BZeZ55tOw8yXZiZs226MMO2nQfTfBkRkcyKG+4OPGpme81sY7Rtqbu/Gt3+LbA0uj0CHC772ZejbXOY2UYzmzCziaNHjyYq9CtT04m2i4j0m7jh/gl3/wjFJpcbzezflz/oxSt+JLrqh7vf6e6j7j46PFx19mxN5w0NJtouItJvYoW7u+ej/48APwUuBV4rNbdE/x+Jnp4Hzi/78WXRttRsWreSwdzAnG2DuQE2rVuZ5suIiGRWw3A3szPM7P2l28CVwK+BHcCG6GkbgAej2zuAr1rRGuDNsuabVKxfPcLt113CyNAgBowMDXL7dZdotIyISCTOUMilwE+LIxxZCPy9u/+jmT0J3GtmNwAvAtdHz3+E4jDIQxSHQv556qWmGPAKcxGR6hqGu7s/D3y4yvbXgSuqbHfgxlRKJyIiTdEMVRGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCFDvczWzAzCbN7GfR/QvM7AkzO2RmY2a2KNp+WnT/UPT4ijaVXUREakhSc/8a8EzZ/e8Ad7j7B4FjwA3R9huAY9H2O6LniYhIB8UKdzNbBlwD/CC6b8DlwH3RU7YD66Pb10b3iR6/Inq+iIh0SNya+3eBvwRORvfPBqbc/UR0/2VgJLo9AhwGiB5/M3r+HGa20cwmzGzi6NGjzZVeRESqahjuZvYZ4Ii7703zhd39TncfdffR4eHhNH+1iEjfWxjjOWuBz5rZ1cDpwB8A3wOGzGxhVDtfBuSj5+eB84GXzWwhcCbweuolFxGRmhrW3N39Vndf5u4rgC8Cu9z9y8Bu4PPR0zYAD0a3d0T3iR7f5e6eaqlFRKSuVsa5/xXwF2Z2iGKb+l3R9ruAs6PtfwFsbq2IIiKSVJxmmVnu/nPg59Ht54FLqzznHeDPUiibiIg0STNURUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEAKdxGRACncRUQCpHAXEQmQwl1EJEANw93MTjezfzGz/WZ2wMy2RNsvMLMnzOyQmY2Z2aJo+2nR/UPR4yvavA8iIlIhTs39XeByd/8wsAq4yszWAN8B7nD3DwLHgBui598AHIu23xE9T0REOqhhuHvRW9HdXPTPgcuB+6Lt24H10e1ro/tEj19hZpZWgUVEpLFYbe5mNmBm+4AjwGPAb4Apdz8RPeVlYCS6PQIcBogefxM4u8rv3GhmE2Y2cfTo0ZZ2QkRE5ooV7u4+4+6rgGXApcBFrb6wu9/p7qPuPjo8PNzqrxMRkTKJRsu4+xSwG/g4MGRmC6OHlgH56HYeOB8gevxM4PU0CisiIvHEGS0zbGZD0e1B4FPAMxRD/vPR0zYAD0a3d0T3iR7f5e6eYplFRKSBhY2fwrnAdjMboHgwuNfdf2ZmTwP/YGbfAiaBu6Ln3wX8HzM7BLwBfLEN5RYRkToahru7/wpYXWX78xTb3yu3vwP8WSqlExGRpmiGqohIgBTuIiIBUriLiARI4S4iEiCFu4hIgBTuIiIBUriLiARI4S4iEiCFu4hIgBTuIiIBUriLiARI4S4iEiCFu4hIgBTuIiIBUriLiARI4S4iEiCFu4hIgBTuIiIBUriLiAQozgWyRaRPjU/m2bbzIK9MTXPe0CCb1q1k/eqRbhdLYlC4i0hV45N5bn3gKaYLMwDkp6a59YGnABTwGaBmGRGpatvOg7PBXjJdmGHbzoNdKpEkoXAXkapemZpOtF16S183y6g9UaS284YGyVcJ8vOGBrtQGkmqb2vupfbE/NQ0zqn2xPHJfLeLJtITNq1byWBuYM62wdwAm9at7FKJJIm+DXe1J4rUt371CLdfdwkjQ4MYMDI0yO3XXaKz24zo22YZtSeKNLZ+9YjCPKP6tuZeq91Q7YkiEoK+DXe1J4pIyPq2WaZ0qqnRMiISor4Nd1B7ooiEq2GzjJmdb2a7zexpMztgZl+Ltp9lZo+Z2XPR/0ui7WZmf2Nmh8zsV2b2kXbvhIiIzBWnzf0EcIu7XwysAW40s4uBzcDj7n4h8Hh0H+DTwIXRv43A91MvNcVx6mu37uKCzQ+zdusujU8XESnTMNzd/VV3/2V0+/fAM8AIcC2wPXradmB9dPta4EdetAcYMrNz0yy0JiCJiNSXqM3dzFYAq4EngKXu/mr00G+BpdHtEeBw2Y+9HG17tWwbZraRYs2e5cuXJyp0vQlIakMXSSbUZThC3a+4Yg+FNLP3AfcDN7n778ofc3cHPMkLu/ud7j7q7qPDw8NJflQTkERSEupZcKj7lUSscDezHMVgv9vdH4g2v1Zqbon+PxJtzwPnl/34smhbajQBSSQdoS7DEep+JRFntIwBdwHPuPtflz20A9gQ3d4APFi2/avRqJk1wJtlzTepqDYByYDLLkp2BiDS70I9Cw51v5KIU3NfC/wn4HIz2xf9uxrYCnzKzJ4D/jS6D/AI8DxwCPhb4L+mXej1q0f43EdHsLJtDty/N99Xp10irQr1LDjU/UoizmiZ/+vu5u4fcvdV0b9H3P11d7/C3S909z919zei57u73+juf+zul7j7RDsK/vCvXp3XyN9vp10irQp1GY5Q9yuJTM5QHZ/Mc+x4oepj/XTaJdKqUJfhCHW/kshkuNernffTaZdIGkJdhiPU/York6tC1qud99Npl4hILZmsuZ85mGNqen6zzGBuQV8fqUWk93RrMlUmw92s+vbTKzpQRKR39OOM0dJkqtKY+9JkKqDt+57JcJ+q0Zlaa7tIVoQagN0MuW7q5lIpmWxzP3Mwl2i7SBaEPGW+X2eMdnMyVSbDvVazTK3tIlmQNACztOx1v84Y7eZkqkyGu5plJERJAjBrtfx+nTHazclUmQz3fv2iSNiSfK/j1vJ7pXbfrzNG168e4fbrLmFkaBADRoYGuf26SzRappZN61bO6ZwByA0Yb797ggs2PxxUR5R0Vyc7OKt9r2sFYJxafq1OzIkX32D3s0c72mmbxRmjaX323ZpMlclwr/yiDC3O8dY7J2bHvvdLT7y0V6dHeCQJwPOGBslXCfjyWn6t2v3de16aXZep2X1qJviyNGO0E599uysOVrzORneNjo76xETz64ut3bqr6hd9ZGiQX2y+vJWiSR/r5e9VZfhAsZZffsp/weaHY19BJ8k+xXntrGv3Z5/We2hme919tNpjmWxzr9SvPfHSXr38vYrTlpukDyrJPvXDsMZ2f/adeA8z2SwDc09pFpgxU+UMRB2s0oo4TR/d1KiZo1obvlH9ephpHAiaDb5enLjV7s++ExWHTNbcK4eBVQv2fuiJl/bK+giParX7L69Z3vI+pTlarVeHdLb7s+/EiL9M1tyrndIADJhx0r1njv6SbVkc4VGpWu1+9ANntbRPSUb1NNLN6fn1tPuzT/M9rCWT4V7r1OWkO/+69ZoOl0ZClqURHnG1uk9pBl+v92u067PvRMUhk+G+eNEAb783v+a+eFE4q0L2YjtkElkvv9SXVvD1er9GO7W74pDJcK8W7PW2Z03WV9DLevnT1OxBrlMHx24fhDvRPNGvMtmhGrqsDzXLevnT0mxnYac6GXuhM7Oy03fJ4hynLVzAzWP7urpcQq8s29AKhXsP6uV2yDiyXv60NHuQq/VzWx46kGrg9MpBeP3qEX6x+XLu+MIq3imcZGq60NWRM71w0EtDcOGe5SNtSdYXRst6+dPS6CBXq3ZY6+eOHS+0HDjlr1mtrbve67dbrxxseqUcrcpkuOfqlDrLR9qSrI+vznr501LvIFevdji0ON5FZ6YLM9xy7/7Y3/PK10xa7nbrlTO+XilHqzIZ7jMxFszo5JE27fa5bi4T2orS+3Dz2D5OW7iAJYtzmSp/2uod5OrVDpMs9zTjHrsiU2t+SLXydUOvnPH1SjlalcnRMidjfvk7caRt18iQXhhfnWQkReX7MDVdYDA3wB1fWNXW/ej2aI966o1lvnlsX9WfaeY7G3fST73fbdD1969XRs70SjlalclwX2DxAr4TR9penWHXqqQHrUbvQymE81PTDERrAY20GCZZGHJZ6yDdaHx3rfbwWuIcFGq9Zi+scgm9MyO4V8rRqkyG+2kLFzBdOFn3OZ060obSPlcp6UGr3vtQGcKltYBaDeM0Dqzdqvk3qh3GXfCrJE5FJgs10l44Y+2lcrQik+HeKNgBPvfRznw4oc6wS3rQqvc+1GvrbeUsJ2kZxyfzbHnoAMeia+0O5hZw4qRTmEnnYJNEnNph+WP1avJxAzqUGqnEk8lwb1SLAbh/b57RD5zV9i9uFmpD5eLWVJMetOq9DzfVaF8uafYsJ0kZxyfzbLpv/2yQQ/VKQjua1Gq95/Vqh5WP1bp4xIBZos7qEGqkEk/D0TJm9kMzO2Jmvy7bdpaZPWZmz0X/L4m2m5n9jZkdMrNfmdlH2lHoOP2pnRwtc9rCU2/jksW5nh0ZkmRyRtLhjLVG+EDxYFxP3KF/lS67aLjq9lempvn6+FNztm3beXBOsNfTaBx6EmlNiKn1efzP6z+c6mXfsj4rU06JU3P/O+B/AT8q27YZeNzdt5rZ5uj+XwGfBi6M/n0M+H70f1ckrREmbX+tdqmsd2I0GXXD+GSeW+7dP2/t+3o11dNzC2b3bWgwx22f/ZO670e1WuHarbsaHozfeucE45P5xNfwHHvycNXHHPjxnpcA+Nb64gEmyXehfBx6q521aXW4t7tJJQud05JMw3B3938ysxUVm68FPhnd3g78nGK4Xwv8yIsXZt1jZkNmdq67v5paiRNI0u7dzJc7KyNlSvtW7aImMD/4qh203j1xcvaxOAEzPpnnth0HZi9aXk/hpHPLvfsB5oysqfcacWri9zxxeDbcG7Vbl8QZh57ks611UMlPTXPB5oc5b2iQyy4aZvezRxu+p+1sUsnKd1nia7bNfWlZYP8WWBrdHgHKq1MvR9vmhbuZbQQ2AixfvrzJYtRX67S9mma+3PX+cLstzmUISyoPgrXei9t2HODdEyfnHAA33bef23Yc4M3pwmwwAWz6yX4KcSckcGoyzsSLbzD25OE5nZyb7jsV/CVxauLl+7xp3cp5be5QbJc8c3GOqeOFOcHa7Dj0ygPT0OLcbAdupVIzTeksA2pXKto9qifUUV/9rOUOVXd3M0swp2725+4E7gQYHR1N9PNxOlQhWadqM1/uWrVBg8TNDGmqNfSwlsqDYK19rlYLL8z47PZSEJ+Y8VifT6XpwsycoCt/jS0PHQCIfcCCYmdjSemzKB8tU6+pqZlRUNXO/nILjNyAxW7vh/mVik40mYQ66qufNbv8wGtmdi5A9P+RaHseOL/secuibamK+2eSpFO1mSnHm9atrNpZ6NDVRYbiTDMvt/vZo3Put/IHXWgy2Bs5drzApp/sr3vd3Epr/mjJnPvrV48w+Y0reWHrNbyw9Rr2ffPKmuHYzPo41d73wknnjEULZzua4yo/wNY6k0qyrkwjWg8oPM2G+w5gQ3R7A/Bg2favRqNm1gBvdqu9vSTuaWUzX+71q0dqBlk3T2eTvnZljW3TupXkFiSJos5I0swD8MLr8/sS4o4GaWZ9n3pnPLPNNIPxRgaVH2Br/d4k68o0ktX1jKS2hs0yZnYPxc7Tc8zsZeCbwFbgXjO7AXgRuD56+iPA1cAh4Djw520ocyJxa6HNjkYY6cHT2bidh+VWbXl0tt38souGG49fzIDyUGymaSNpB2a9973Uvp4bMHILrO6BKjdgs5WK8cl83SaoNDs9NQY+LHFGy3ypxkNXVHmuAze2Wqi0JD2tbObLnfYkpjQ6zmqV6XMfHeHuPS9VPdsobzev1u6dReUH2FZGg8T9TKq975UKM86SxTkWL1rIK1PTDC3O8ebxAnMG0Pqp1603yqkkaSevZqX2h0zOUM0tgEbDyVtdlKqaen8kafzxpNFxVirjdGGm6gJdoQR3I+W1X6g/smnt1l01hyNW+0yqjRAqrxiUvgu1InnqeIHJb1wJFOcBVI6mKZz02T6bOH0nSTt5NX69P2Qy3E/EaHrNT01zy737mXjxjdmxzpVaWdK28o8kjT+Ueh1nN4/tS1zGGffZs4jSzyypMzQvJCcqRqfUazKpNxyxaidpxQih0hDO3c8enV31Mu4iX60OQcwtsMSdvBq/3h8yebGOuBczmHHnx3temjcVHZJPC+/EpbfqdZylUcbxyTxvvXMitfL2Moc571W1DvN6Su9bnL6L6cIMd+95afa59ZpRBirCuN4orTj9Nu87fWHdkI5zKT0tOxCmTNbck7rnicOz/9f7wysPwvLZlfVqu62Oikky2ahUxtt2HEi07G7pD3zbzoOJR5xkWfnnWdlUFccrZWvPNxL3XZ056Uy8+Mbs55d06d9KU3XOwsYn8zXnhJQOHGq2CVcma+5JlWrwcf5I81PTbPrJ/jkTduo1Y7QyKqby7CFu6ExNF6rWrmqVpTSpqh9nG5bCKk6tutLQ4lyi58d1d1kTUOUQxKHBHKfnFnDz2D627TzI5z46wkid71i979+2nQerBrvB7MEjlItBy3x9UXNPYsDqD1Mrl2RUTLX2/aSTjcpteejAvN+3ad1Kbh7bN+8PujSpqpkhkllRb9ZyM+/xwAJrWxOWM3cGc6nPploteuzJw5yxqPhnWrmPjb5/tQ7mzqlauZYdCFdf1NyTSFJTmy7McNPYPlZtebRuO2VpLfHy9v2bxva1FLTHjhfm9RdA7YDLT01z/L0TwX7gadevZ056w4N8abJPM8prxuOTeVZteZSbxvbV7bx1Tk0/iDPJqFatvrzMoVwMWuZTzT0FU9MFbhrbx01j+2av71o+/HDLQwcSrS3SjFJbfD39MEqmk/516zVA7Qtp1FO+ZnySRdac+Nc8jTMHI2sXm5H4FO4pK/2Nlmrnja5ClKY4y+tKelZsfpgL//AMLrtoeN7ksNyCYkdsrcwu1Yyb6eSO22QSZw6GLr0XLoW7SAueO/I2zx15e972Sy9YwtOv/r7q2VL5BKtm2raTNJnEmYOhZQfCFGoTrEhX/eI3b1QN9iWLc2z7/KlL4yVt21aTicSlcBfpkCWLc0x+Y+4yw5vWraz5R5gbML6yZrlWapSmqFlGpEOOHS9UvYjLwIBxsqLD/YxFA3z7PyjIpXmquYt0UOXkoFrXgh1avEjBLi1RuIt0UGUHqiYRSbso3EU6qLIDVZOIpF0U7iIpMYqdprUuUVhtpIuuXSrtog5V6WtnLBrg7feaW9+nXPms0dI6QvmyVSVrXTxGk4ikXRTu0ndyA8YX/t35s1deGhka5Ph7J+ouz1AK78rFvWB+TTvppCBNIpJ2ULhL0Aw4PbeA6ei6jEsW57jmQ+dy/978nNUXcwuM3IBVHblSHt6qaUtWKNwlWIO5gaqTftZu3TV/9cWTztBgjjNOW9iwOUU1bckChbsEpbTmeb0LpNcaZvjmdIF937yyvQUU6RCFu2SeQaLmkVoXLdHwQwmJwl0yLe7a5uW0hrn0A4W7ZFazgRy3U7TapRHV1i5ZoXCXTCpvU28mhBt1ila7nmnpUoatBHx5WYcW53AvtvXr4CFpU7hLRwwN5ijMnGx5wtDQYI7bPvsnsyHYrhCudvHy6cIM23YebPr3Vpa1fFx9WuUWKdHyA9IRU9OFVGaCTk0XuHlsH18fLwZhvRBuRTsW9KpW1nJplFukRDV3yRwHfrznpXnXLS3X6qqK9UbUNNsWH6dMaa0Gqf4CUc1dMqveZaVbHdZYa0Gvyy4a5tYHniI/NY1zqjllfDLf8HfGKVMawzFLzT/NlFHCoXCX4KQxrHH96hFuv+6SeZe42/3s0aabgaodMNIuN7SvqUqypS3NMmZ2FfA9YAD4gbtvbcfriJSMDA2m3gRRbUTNzWP7qj43TnNK5RDMdo2W0QVABNoQ7mY2APxv4FPAy8CTZrbD3Z9O+7VEAAbMEk9kalars1s7sS6NZuAKtKdZ5lLgkLs/7+7vAf8AXNuG15EOGcwN8N0vrOp2MWr60sfO79hrZeHiGlkoo7RfO8J9BDhcdv/laNscZrbRzCbMbOLo0aNtKIa0onQtoVJb8/rVI4z0YM3vK2uW8631l3Ts9Wq1xffSSJQslFHar2tDId39TuBOgNHR0XoDHySBpe9fxO/emak7nrqRyolCJdXWZKmltD768Wgd9TQZ8OUOh3q5LCz5m4UySnu1I9zzQPl58rJoW2q+smY5P97zUpq/siUDBn8wmKt7JZ+5zy+uFb5kcY53CzOzAVgtVL8+/hT3PHGYGZ97/CstbVtu7R+fxd3/5eN1xzhXPnbZRcOzVyRq1KlX2SF45mAOM5g6XqjZOVhrun2155f/bo3NFmmNuadbaTazhcD/A66gGOpPAv/R3Q/U+pnR0VGfmJhI9DrloTdgxpc+dn7XanK1aCKJiLSTme1199Gqj6Ud7tELXg18l+JQyB+6+7frPb+ZcBcR6Xf1wr0tbe7u/gjwSDt+t4iINKYZqiIiAVK4i4gESOEuIhIghbuISIDaMlomcSHMjgIvNvnj5wD/lmJxelU/7Kf2MRz9sJ+9sI8fcPfhag/0RLi3wswmag0FCkk/7Kf2MRz9sJ+9vo9qlhERCZDCXUQkQCGE+53dLkCH9MN+ah/D0Q/72dP7mPk2dxERmS+EmruIiFRQuIuIBCjT4W5mV5nZQTM7ZGabu12eNJjZD83siJn9umzbWWb2mJk9F/2/pJtlbJWZnW9mu83saTM7YGZfi7aHtp+nm9m/mNn+aD+3RNsvMLMnou/tmJkt6nZZW2VmA2Y2aWY/i+6HuI8vmNlTZrbPzCaibT37nc1suJddiPvTwMXAl8zs4u6WKhV/B1xVsW0z8Li7Xwg8Ht3PshPALe5+MbAGuDH67ELbz3eBy939w8Aq4CozWwN8B7jD3T8IHANu6F4RU/M14Jmy+yHuI8Bl7r6qbHx7z35nMxvuBHohbnf/J+CNis3XAtuj29uB9Z0sU9rc/VV3/2V0+/cUQ2GE8PbT3f2t6G4u+ufA5cB90fbM76eZLQOuAX4Q3TcC28c6evY7m+Vwj3Uh7kAsdfdXo9u/BZZ2szBpMrMVwGrgCQLcz6i5Yh9wBHgM+A0w5e4noqeE8L39LvCXQOmCuWcT3j5C8cD8qJntNbON0bae/c527QLZ0hx3dzMLYvyqmb0PuB+4yd1/V6zwFYWyn+4+A6wysyHgp8BF3S1RuszsM8ARd99rZp/scnHa7RPunjezPwQeM7Nnyx/ste9slmvubb8Qdw95zczOBYj+P9Ll8rTMzHIUg/1ud38g2hzcfpa4+xSwG/g4MBRdaxiy/71dC3zWzF6g2DR6OfA9wtpHANw9H/1/hOKB+lJ6+Dub5XB/Ergw6pVfBHwR2NHlMrXLDmBDdHsD8GAXy9KyqE32LuAZd//rsodC28/hqMaOmQ0Cn6LYv7Ab+Hz0tEzvp7vf6u7L3H0Fxb/BXe7+ZQLaRwAzO8PM3l+6DVwJ/Joe/s5meoZq0gtxZ4GZ3QN8kuJyoq8B3wTGgXuB5RSXRr7e3Ss7XTPDzD4B/DPwFKfaaf87xXb3kPbzQxQ72QYoVqTudff/YWZ/RLGWexYwCXzF3d/tXknTETXL/Dd3/0xo+xjtz0+juwuBv3f3b5vZ2fTodzbT4S4iItVluVlGRERqULiLiARI4S4iEiCFu4hIgBTuIiIBUriLiARI4S4iEqD/D+0woBVcDp1tAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "mlp.scatter(df['distance'],df['fare_amount'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "97cb9dde",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.drop(df[(df['fare_amount']>100) & (df['distance']<1)].index,inplace=True)\n",
    "df.drop(df[(df['distance']>100) & (df['fare_amount']<100)].index,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "55cd075f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2070d7e5660>"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "mlp.scatter(df['distance'],df['fare_amount'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "525e8b7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "corr=df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "59bb0196",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>fare_amount</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>distance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>fare_amount</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011970</td>\n",
       "      <td>-0.008610</td>\n",
       "      <td>0.010464</td>\n",
       "      <td>-0.008621</td>\n",
       "      <td>0.012949</td>\n",
       "      <td>0.884952</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pickup_longitude</th>\n",
       "      <td>0.011970</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.949098</td>\n",
       "      <td>0.999883</td>\n",
       "      <td>-0.993974</td>\n",
       "      <td>0.009175</td>\n",
       "      <td>0.005355</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pickup_latitude</th>\n",
       "      <td>-0.008610</td>\n",
       "      <td>-0.949098</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.949094</td>\n",
       "      <td>0.954759</td>\n",
       "      <td>-0.009219</td>\n",
       "      <td>0.003202</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <td>0.010464</td>\n",
       "      <td>0.999883</td>\n",
       "      <td>-0.949094</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.993961</td>\n",
       "      <td>0.009169</td>\n",
       "      <td>0.004425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <td>-0.008621</td>\n",
       "      <td>-0.993974</td>\n",
       "      <td>0.954759</td>\n",
       "      <td>-0.993961</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.009266</td>\n",
       "      <td>-0.002150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>passenger_count</th>\n",
       "      <td>0.012949</td>\n",
       "      <td>0.009175</td>\n",
       "      <td>-0.009219</td>\n",
       "      <td>0.009169</td>\n",
       "      <td>-0.009266</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.007746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>distance</th>\n",
       "      <td>0.884952</td>\n",
       "      <td>0.005355</td>\n",
       "      <td>0.003202</td>\n",
       "      <td>0.004425</td>\n",
       "      <td>-0.002150</td>\n",
       "      <td>0.007746</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   fare_amount  pickup_longitude  pickup_latitude  \\\n",
       "fare_amount           1.000000          0.011970        -0.008610   \n",
       "pickup_longitude      0.011970          1.000000        -0.949098   \n",
       "pickup_latitude      -0.008610         -0.949098         1.000000   \n",
       "dropoff_longitude     0.010464          0.999883        -0.949094   \n",
       "dropoff_latitude     -0.008621         -0.993974         0.954759   \n",
       "passenger_count       0.012949          0.009175        -0.009219   \n",
       "distance              0.884952          0.005355         0.003202   \n",
       "\n",
       "                   dropoff_longitude  dropoff_latitude  passenger_count  \\\n",
       "fare_amount                 0.010464         -0.008621         0.012949   \n",
       "pickup_longitude            0.999883         -0.993974         0.009175   \n",
       "pickup_latitude            -0.949094          0.954759        -0.009219   \n",
       "dropoff_longitude           1.000000         -0.993961         0.009169   \n",
       "dropoff_latitude           -0.993961          1.000000        -0.009266   \n",
       "passenger_count             0.009169         -0.009266         1.000000   \n",
       "distance                    0.004425         -0.002150         0.007746   \n",
       "\n",
       "                   distance  \n",
       "fare_amount        0.884952  \n",
       "pickup_longitude   0.005355  \n",
       "pickup_latitude    0.003202  \n",
       "dropoff_longitude  0.004425  \n",
       "dropoff_latitude  -0.002150  \n",
       "passenger_count    0.007746  \n",
       "distance           1.000000  "
      ]
     },
     "execution_count": 96,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e46907f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "id": "66974cd8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "114a3dbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "corr=df.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "id": "e0e431ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>fare_amount</th>\n",
       "      <th>pickup_longitude</th>\n",
       "      <th>pickup_latitude</th>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <th>passenger_count</th>\n",
       "      <th>distance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>fare_amount</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.011970</td>\n",
       "      <td>-0.008610</td>\n",
       "      <td>0.010464</td>\n",
       "      <td>-0.008621</td>\n",
       "      <td>0.012949</td>\n",
       "      <td>0.884952</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pickup_longitude</th>\n",
       "      <td>0.011970</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.949098</td>\n",
       "      <td>0.999883</td>\n",
       "      <td>-0.993974</td>\n",
       "      <td>0.009175</td>\n",
       "      <td>0.005355</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pickup_latitude</th>\n",
       "      <td>-0.008610</td>\n",
       "      <td>-0.949098</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.949094</td>\n",
       "      <td>0.954759</td>\n",
       "      <td>-0.009219</td>\n",
       "      <td>0.003202</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dropoff_longitude</th>\n",
       "      <td>0.010464</td>\n",
       "      <td>0.999883</td>\n",
       "      <td>-0.949094</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.993961</td>\n",
       "      <td>0.009169</td>\n",
       "      <td>0.004425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>dropoff_latitude</th>\n",
       "      <td>-0.008621</td>\n",
       "      <td>-0.993974</td>\n",
       "      <td>0.954759</td>\n",
       "      <td>-0.993961</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>-0.009266</td>\n",
       "      <td>-0.002150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>passenger_count</th>\n",
       "      <td>0.012949</td>\n",
       "      <td>0.009175</td>\n",
       "      <td>-0.009219</td>\n",
       "      <td>0.009169</td>\n",
       "      <td>-0.009266</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.007746</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>distance</th>\n",
       "      <td>0.884952</td>\n",
       "      <td>0.005355</td>\n",
       "      <td>0.003202</td>\n",
       "      <td>0.004425</td>\n",
       "      <td>-0.002150</td>\n",
       "      <td>0.007746</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                   fare_amount  pickup_longitude  pickup_latitude  \\\n",
       "fare_amount           1.000000          0.011970        -0.008610   \n",
       "pickup_longitude      0.011970          1.000000        -0.949098   \n",
       "pickup_latitude      -0.008610         -0.949098         1.000000   \n",
       "dropoff_longitude     0.010464          0.999883        -0.949094   \n",
       "dropoff_latitude     -0.008621         -0.993974         0.954759   \n",
       "passenger_count       0.012949          0.009175        -0.009219   \n",
       "distance              0.884952          0.005355         0.003202   \n",
       "\n",
       "                   dropoff_longitude  dropoff_latitude  passenger_count  \\\n",
       "fare_amount                 0.010464         -0.008621         0.012949   \n",
       "pickup_longitude            0.999883         -0.993974         0.009175   \n",
       "pickup_latitude            -0.949094          0.954759        -0.009219   \n",
       "dropoff_longitude           1.000000         -0.993961         0.009169   \n",
       "dropoff_latitude           -0.993961          1.000000        -0.009266   \n",
       "passenger_count             0.009169         -0.009266         1.000000   \n",
       "distance                    0.004425         -0.002150         0.007746   \n",
       "\n",
       "                   distance  \n",
       "fare_amount        0.884952  \n",
       "pickup_longitude   0.005355  \n",
       "pickup_latitude    0.003202  \n",
       "dropoff_longitude  0.004425  \n",
       "dropoff_latitude  -0.002150  \n",
       "passenger_count    0.007746  \n",
       "distance           1.000000  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "e8b84d61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(corr,cmap='Reds')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "e0523a85",
   "metadata": {},
   "outputs": [],
   "source": [
    "X=df['distance'].values.reshape(-1,1)\n",
    "Y=df['fare_amount'].values.reshape(-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "bfc1fc10",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "66b70846",
   "metadata": {},
   "outputs": [],
   "source": [
    "std=StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "id": "ba2907ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_std=std.fit_transform(X)\n",
    "y_std=std.fit_transform(Y)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "16bf5b33",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "e28e8f39",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x_std,y_std,test_size=0.2,random_state=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "0c8dc0a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "id": "1f0f68b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "regr=LinearRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "398b95e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LinearRegression()"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regr.fit(x_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "id": "cc02be33",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred=regr.predict(x_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "20f9d9c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 2.03841588],\n",
       "       [-0.47141641],\n",
       "       [-0.04460099],\n",
       "       ...,\n",
       "       [-0.33756876],\n",
       "       [-0.50619352],\n",
       "       [-0.52596473]])"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pred"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "97f1db68",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 2.26826117],\n",
       "       [-0.46344493],\n",
       "       [-0.03432635],\n",
       "       ...,\n",
       "       [-0.42157971],\n",
       "       [-0.58904062],\n",
       "       [-0.40064709]])"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "2409cde4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.7903591348178967"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "regr.score(x_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d90dc4f5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0d5053a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
