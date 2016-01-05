#!/Users/didionjp/anaconda/envs/py35/bin/python

import mhcpredict.predict
import mhcpredict.util

#if __name__ == "__main__":
result = mhcpredict.predict.predictPeptides(
    "VIFRLMRTNFL", 
    alleles="HLA-DRB1*0101", 
    config=mhcpredict.util.DictConfig(dict(NetMHCIIpan=dict(
        executable="/Users/didionjp/Downloads/netMHCIIpan-3.1/netMHCIIpan",
        tempdir=".")))
)
    result.to_csv("output.txt", sep="\t")