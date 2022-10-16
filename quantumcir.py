#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import *


# In[4]:


qr=QuantumRegister(2)


# In[5]:


er=ClassicalRegister(2)


# In[6]:


circuit=QuantumCircuit(qr,er)


# In[7]:


circuit.draw()


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


circuit.draw(output='mpl')


# In[10]:


circuit.h(qr[0])


# In[11]:


circuit.draw(output='mpl')


# In[12]:


circuit.cx(qr[0],qr[1])


# In[13]:


circuit.draw(output='mpl')


# In[14]:


circuit.measure(qr,er)


# In[15]:


circuit.draw(output='mpl')


# In[16]:


simulator=Aer.get_backend('qasm_simulator')


# In[17]:


result=execute(circuit,backend=simulator).result()


# In[18]:


from qiskit.tools.visualization import plot_histogram


# In[20]:


plot_histogram(result.get_counts(circuit))


# In[ ]:




