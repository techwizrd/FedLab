��          L               |   K   }      �      �      �   �     w  �  G   "     j     }     �  ~   �   **A standard implementation of this part is in :class:`ClientSGDTrainer`.** Client local training Federated Optimization Server global aggregation You can overwrite ``_update_model(model_parameters_list)`` to customize aggregation procedure. Typically, you can define aggregation functions as FedLab. Project-Id-Version: FedLab 
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2021-10-30 17:11+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: zh_CN
Language-Team: zh_CN <LL@li.org>
Plural-Forms: nplurals=1; plural=0
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.9.0
 这部分的一个标准实现可以参考 :class:`ClientSGDTrainer`。 Client本地训练 联邦优化 Server的全局聚合 你可以通过复写 ``_update_model(model_parameters_list)`` 来自定义聚合过程。通常你可以定义聚合函数。 