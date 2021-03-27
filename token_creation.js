const GrpcClient = require('grpc-bchrpc-node');
const bitcore = require('bitcore-lib-cash');
const slpMdm = require('slp-mdm');
const grpc = new GrpcClient.GrpcClient({ url: 'bchd.fountainhead.cash:443'});


var privateKey = new bitcore.PrivateKey('***');

var inputUtxos = {
    "txId" : "115e8f72f39fad874cfab0deed11a80f24f967a84079fb56ddf53ea02e308986",
    "tokenId": "***",
    "outputIndex" : 0,
    "address" : "bitcoincash:***",
    "script" : "76a91447862fe165e6121af80d5dde1ecb478ed170565b88ac",
    "satoshis": 10

  };

toAddress = "bitcoincash:***"



  const tx = new bitcore.Transaction()          
        .from(inputUtxos)                         
        .addOutput(new bitcore.Transaction.Output({
            script: bitcore.Script.fromBuffer(slpMdm.NFT1.Child.genesis(    
            'CryptoYellow',                                         
            'CRYELLOW',                                             
            'https://github.com/steffanjensen/cryptoart',         
            'f8bf41177a5f5e808a7ccb648b51080b031f15ca8018d91a576263d6cc626eb6'    )),
            satoshis: 0 
        }))                                   
        .to(toAddress, 546)                          
        .sign(privateKey);
console.log(tx)
