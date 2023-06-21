import numpy as np
import pandas as pd
from datetime import datetime

def joinFeatures(dictsList,audioNameList):

	numero = 1000

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(f"Joining features...:  {current_time}")

	length = len(dictsList)
	globalFM = np.empty((0,6381))

	globalFM0 = np.empty((0,6381))
	globalFM1 = np.empty((0,6381))
	globalFM2 = np.empty((0,6381))
	globalFM3 = np.empty((0,6381))
	globalFM4 = np.empty((0,6381))
	globalFM5 = np.empty((0,6381))
	globalFM6 = np.empty((0,6381))
	globalFM7 = np.empty((0,6381))
	globalFM8 = np.empty((0,6381))
	globalFM9 = np.empty((0,6381))
	globalFM10 = np.empty((0,6381))
	globalFM11 = np.empty((0,6381))
	globalFM12 = np.empty((0,6381))
	globalFM13 = np.empty((0,6381))
	globalFM14 = np.empty((0,6381))
	globalFM15 = np.empty((0,6381))
	globalFM16 = np.empty((0,6381))
	globalFM17 = np.empty((0,6381))
	globalFM18 = np.empty((0,6381))
	globalFM19 = np.empty((0,6381))
	globalFM20 = np.empty((0,6381))
	globalFM21 = np.empty((0,6381))
	globalFM22 = np.empty((0,6381))
	globalFM23 = np.empty((0,6381))
	globalFM24 = np.empty((0,6381))
	globalFM25 = np.empty((0,6381))
	globalFM26 = np.empty((0,6381))
	globalFM27 = np.empty((0,6381))
	globalFM28 = np.empty((0,6381))
	globalFM29 = np.empty((0,6381))
	globalFM30 = np.empty((0,6381))
	globalFM31 = np.empty((0,6381))
	globalFM32 = np.empty((0,6381))
	globalFM33 = np.empty((0,6381))
	globalFM34 = np.empty((0,6381))
	globalFM35 = np.empty((0,6381))
	globalFM36 = np.empty((0,6381))
	globalFM37 = np.empty((0,6381))
	globalFM38 = np.empty((0,6381))
	globalFM39 = np.empty((0,6381))
	globalFM40 = np.empty((0,6381))
	globalFM41 = np.empty((0,6381))
	globalFM42 = np.empty((0,6381))
	globalFM43 = np.empty((0,6381))
	globalFM44 = np.empty((0,6381))
	globalFM45 = np.empty((0,6381))
	globalFM46 = np.empty((0,6381))
	globalFM47 = np.empty((0,6381))
	globalFM48 = np.empty((0,6381))
	globalFM49 = np.empty((0,6381))
	globalFM50 = np.empty((0,6381))
	globalFM51 = np.empty((0,6381))
	globalFM52 = np.empty((0,6381))
	globalFM53 = np.empty((0,6381))
	globalFM54 = np.empty((0,6381))
	globalFM55 = np.empty((0,6381))
	globalFM56 = np.empty((0,6381))
	globalFM57 = np.empty((0,6381))
	globalFM58 = np.empty((0,6381))
	globalFM59 = np.empty((0,6381))
	globalFM60 = np.empty((0,6381))
	globalFM61 = np.empty((0,6381))
	globalFM62 = np.empty((0,6381))
	globalFM63 = np.empty((0,6381))
	globalFM64 = np.empty((0,6381))
	globalFM65 = np.empty((0,6381))
	globalFM66 = np.empty((0,6381))
	globalFM67 = np.empty((0,6381))
	globalFM68 = np.empty((0,6381))
	globalFM69 = np.empty((0,6381))
	globalFM70 = np.empty((0,6381))
	globalFM71 = np.empty((0,6381))
	globalFM72 = np.empty((0,6381))
	globalFM73 = np.empty((0,6381))
	globalFM74 = np.empty((0,6381))
	globalFM75 = np.empty((0,6381))
	globalFM76 = np.empty((0,6381))
	globalFM77 = np.empty((0,6381))
	globalFM78 = np.empty((0,6381))
	globalFM79 = np.empty((0,6381))
	globalFM80 = np.empty((0,6381))
	globalFM81 = np.empty((0,6381))
	globalFM82 = np.empty((0,6381))
	globalFM83 = np.empty((0,6381))
	globalFM84 = np.empty((0,6381))
	globalFM85 = np.empty((0,6381))
	globalFM86 = np.empty((0,6381))
	globalFM87 = np.empty((0,6381))
	globalFM88 = np.empty((0,6381))
	globalFM89 = np.empty((0,6381))
	globalFM90 = np.empty((0,6381))
	globalFM91 = np.empty((0,6381))
	globalFM92 = np.empty((0,6381))
	globalFM93 = np.empty((0,6381))
	globalFM94 = np.empty((0,6381))
	globalFM95 = np.empty((0,6381))
	globalFM96 = np.empty((0,6381))
	globalFM97 = np.empty((0,6381))
	globalFM98 = np.empty((0,6381))
	globalFM99 = np.empty((0,6381))
	globalFM100 = np.empty((0,6381))
	globalFM101 = np.empty((0,6381))
	globalFM102 = np.empty((0,6381))
	globalFM103 = np.empty((0,6381))
	globalFM104 = np.empty((0,6381))
	globalFM105 = np.empty((0,6381))
	globalFM106 = np.empty((0,6381))
	globalFM107 = np.empty((0,6381))
	globalFM108 = np.empty((0,6381))
	globalFM109 = np.empty((0,6381))
	globalFM110 = np.empty((0,6381))
	globalFM111 = np.empty((0,6381))
	globalFM112 = np.empty((0,6381))
	globalFM113 = np.empty((0,6381))
	globalFM114 = np.empty((0,6381))
	globalFM115 = np.empty((0,6381))
	globalFM116 = np.empty((0,6381))
	globalFM117 = np.empty((0,6381))
	globalFM118 = np.empty((0,6381))
	globalFM119 = np.empty((0,6381))
	globalFM120 = np.empty((0,6381))
	globalFM121 = np.empty((0,6381))
	globalFM122 = np.empty((0,6381))
	globalFM123 = np.empty((0,6381))
	globalFM124 = np.empty((0,6381))
	globalFM125 = np.empty((0,6381))
	globalFM126 = np.empty((0,6381))
	globalFM127 = np.empty((0,6381))
	globalFM128 = np.empty((0,6381))
	globalFM129 = np.empty((0,6381))
	globalFM130 = np.empty((0,6381))
	globalFM131 = np.empty((0,6381))
	globalFM132 = np.empty((0,6381))
	globalFM133 = np.empty((0,6381))
	globalFM134 = np.empty((0,6381))
	globalFM135 = np.empty((0,6381))
	globalFM136 = np.empty((0,6381))
	globalFM137 = np.empty((0,6381))
	globalFM138 = np.empty((0,6381))
	globalFM139 = np.empty((0,6381))
	globalFM140 = np.empty((0,6381))
	globalFM141 = np.empty((0,6381))
	globalFM142 = np.empty((0,6381))
	globalFM143 = np.empty((0,6381))
	globalFM144 = np.empty((0,6381))
	globalFM145 = np.empty((0,6381))
	globalFM146 = np.empty((0,6381))
	globalFM147 = np.empty((0,6381))
	globalFM148 = np.empty((0,6381))
	globalFM149 = np.empty((0,6381))
	globalFM150 = np.empty((0,6381))
	globalFM151 = np.empty((0,6381))
	globalFM152 = np.empty((0,6381))
	globalFM153 = np.empty((0,6381))
	globalFM154 = np.empty((0,6381))
	globalFM155 = np.empty((0,6381))
	globalFM156 = np.empty((0,6381))
	globalFM157 = np.empty((0,6381))
	globalFM158 = np.empty((0,6381))
	globalFM159 = np.empty((0,6381))
	globalFM160 = np.empty((0,6381))
	globalFM161 = np.empty((0,6381))
	globalFM162 = np.empty((0,6381))
	globalFM163 = np.empty((0,6381))
	globalFM164 = np.empty((0,6381))
	globalFM165 = np.empty((0,6381))
	globalFM166 = np.empty((0,6381))
	globalFM167 = np.empty((0,6381))
	globalFM168 = np.empty((0,6381))
	globalFM169 = np.empty((0,6381))
	globalFM170 = np.empty((0,6381))
	globalFM171 = np.empty((0,6381))
	globalFM172 = np.empty((0,6381))
	globalFM173 = np.empty((0,6381))
	globalFM174 = np.empty((0,6381))
	globalFM175 = np.empty((0,6381))
	globalFM176 = np.empty((0,6381))
	globalFM177 = np.empty((0,6381))
	globalFM178 = np.empty((0,6381))
	globalFM179 = np.empty((0,6381))
	globalFM180 = np.empty((0,6381))
	globalFM181 = np.empty((0,6381))
	globalFM182 = np.empty((0,6381))
	globalFM183 = np.empty((0,6381))
	globalFM184 = np.empty((0,6381))
	globalFM185 = np.empty((0,6381))
	globalFM186 = np.empty((0,6381))
	globalFM187 = np.empty((0,6381))
	globalFM188 = np.empty((0,6381))
	globalFM189 = np.empty((0,6381))
	globalFM190 = np.empty((0,6381))
	globalFM191 = np.empty((0,6381))
	globalFM192 = np.empty((0,6381))
	globalFM193 = np.empty((0,6381))
	globalFM194 = np.empty((0,6381))
	globalFM195 = np.empty((0,6381))
	globalFM196 = np.empty((0,6381))
	globalFM197 = np.empty((0,6381))
	globalFM198 = np.empty((0,6381))
	globalFM199 = np.empty((0,6381))
	globalFM200 = np.empty((0,6381))
	globalFM201 = np.empty((0,6381))
	globalFM202 = np.empty((0,6381))
	globalFM203 = np.empty((0,6381))
	globalFM204 = np.empty((0,6381))
	globalFM205 = np.empty((0,6381))
	globalFM206 = np.empty((0,6381))
	globalFM207 = np.empty((0,6381))
	globalFM208 = np.empty((0,6381))
	globalFM209 = np.empty((0,6381))
	globalFM210 = np.empty((0,6381))
	globalFM211 = np.empty((0,6381))
	globalFM212 = np.empty((0,6381))
	globalFM213 = np.empty((0,6381))
	globalFM214 = np.empty((0,6381))
	globalFM215 = np.empty((0,6381))
	globalFM216 = np.empty((0,6381))
	globalFM217 = np.empty((0,6381))
	globalFM218 = np.empty((0,6381))
	globalFM219 = np.empty((0,6381))
	globalFM220 = np.empty((0,6381))
	globalFM221 = np.empty((0,6381))
	globalFM222 = np.empty((0,6381))
	globalFM223 = np.empty((0,6381))
	globalFM224 = np.empty((0,6381))
	globalFM225 = np.empty((0,6381))
	globalFM226 = np.empty((0,6381))
	globalFM227 = np.empty((0,6381))
	globalFM228 = np.empty((0,6381))
	globalFM229 = np.empty((0,6381))
	globalFM230 = np.empty((0,6381))
	globalFM231 = np.empty((0,6381))
	globalFM232 = np.empty((0,6381))
	globalFM233 = np.empty((0,6381))
	globalFM234 = np.empty((0,6381))
	globalFM235 = np.empty((0,6381))
	globalFM236 = np.empty((0,6381))
	globalFM237 = np.empty((0,6381))
	globalFM238 = np.empty((0,6381))
	globalFM239 = np.empty((0,6381))
	globalFM240 = np.empty((0,6381))
	globalFM241 = np.empty((0,6381))
	globalFM242 = np.empty((0,6381))
	globalFM243 = np.empty((0,6381))
	globalFM244 = np.empty((0,6381))
	globalFM245 = np.empty((0,6381))
	globalFM246 = np.empty((0,6381))
	globalFM247 = np.empty((0,6381))
	globalFM248 = np.empty((0,6381))
	globalFM249 = np.empty((0,6381))
	globalFM250 = np.empty((0,6381))
	globalFM251 = np.empty((0,6381))
	globalFM252 = np.empty((0,6381))
	globalFM253 = np.empty((0,6381))
	globalFM254 = np.empty((0,6381))
	globalFM255 = np.empty((0,6381))
	globalFM256 = np.empty((0,6381))
	globalFM257 = np.empty((0,6381))
	globalFM258 = np.empty((0,6381))
	globalFM259 = np.empty((0,6381))
	globalFM260 = np.empty((0,6381))
	globalFM261 = np.empty((0,6381))
	globalFM262 = np.empty((0,6381))
	globalFM263 = np.empty((0,6381))
	globalFM264 = np.empty((0,6381))
	globalFM265 = np.empty((0,6381))
	globalFM266 = np.empty((0,6381))
	globalFM267 = np.empty((0,6381))
	globalFM268 = np.empty((0,6381))
	globalFM269 = np.empty((0,6381))
	globalFM270 = np.empty((0,6381))
	globalFM271 = np.empty((0,6381))
	globalFM272 = np.empty((0,6381))
	globalFM273 = np.empty((0,6381))
	globalFM274 = np.empty((0,6381))
	globalFM275 = np.empty((0,6381))
	globalFM276 = np.empty((0,6381))
	globalFM277 = np.empty((0,6381))
	globalFM278 = np.empty((0,6381))
	globalFM279 = np.empty((0,6381))
	globalFM280 = np.empty((0,6381))
	globalFM281 = np.empty((0,6381))
	globalFM282 = np.empty((0,6381))
	globalFM283 = np.empty((0,6381))
	globalFM284 = np.empty((0,6381))
	globalFM285 = np.empty((0,6381))
	globalFM286 = np.empty((0,6381))
	globalFM287 = np.empty((0,6381))
	globalFM288 = np.empty((0,6381))
	globalFM289 = np.empty((0,6381))
	globalFM290 = np.empty((0,6381))
	globalFM291 = np.empty((0,6381))
	globalFM292 = np.empty((0,6381))
	globalFM293 = np.empty((0,6381))
	globalFM294 = np.empty((0,6381))
	globalFM295 = np.empty((0,6381))
	globalFM296 = np.empty((0,6381))
	globalFM297 = np.empty((0,6381))
	globalFM298 = np.empty((0,6381))
	globalFM299 = np.empty((0,6381))
	globalFM300 = np.empty((0,6381))
	globalFM301 = np.empty((0,6381))
	globalFM302 = np.empty((0,6381))
	globalFM303 = np.empty((0,6381))
	globalFM304 = np.empty((0,6381))
	globalFM305 = np.empty((0,6381))
	globalFM306 = np.empty((0,6381))
	globalFM307 = np.empty((0,6381))
	globalFM308 = np.empty((0,6381))
	globalFM309 = np.empty((0,6381))
	globalFM310 = np.empty((0,6381))
	globalFM311 = np.empty((0,6381))
	globalFM312 = np.empty((0,6381))
	globalFM313 = np.empty((0,6381))
	globalFM314 = np.empty((0,6381))
	globalFM315 = np.empty((0,6381))
	globalFM316 = np.empty((0,6381))
	globalFM317 = np.empty((0,6381))
	globalFM318 = np.empty((0,6381))
	globalFM319 = np.empty((0,6381))
	globalFM320 = np.empty((0,6381))
	globalFM321 = np.empty((0,6381))
	globalFM322 = np.empty((0,6381))
	globalFM323 = np.empty((0,6381))
	globalFM324 = np.empty((0,6381))
	globalFM325 = np.empty((0,6381))
	globalFM326 = np.empty((0,6381))
	globalFM327 = np.empty((0,6381))
	globalFM328 = np.empty((0,6381))
	globalFM329 = np.empty((0,6381))
	globalFM330 = np.empty((0,6381))
	globalFM331 = np.empty((0,6381))
	globalFM332 = np.empty((0,6381))
	globalFM333 = np.empty((0,6381))
	globalFM334 = np.empty((0,6381))
	globalFM335 = np.empty((0,6381))
	globalFM336 = np.empty((0,6381))
	globalFM337 = np.empty((0,6381))
	globalFM338 = np.empty((0,6381))
	globalFM339 = np.empty((0,6381))
	globalFM340 = np.empty((0,6381))
	globalFM341 = np.empty((0,6381))
	globalFM342 = np.empty((0,6381))
	globalFM343 = np.empty((0,6381))
	globalFM344 = np.empty((0,6381))
	globalFM345 = np.empty((0,6381))
	globalFM346 = np.empty((0,6381))
	globalFM347 = np.empty((0,6381))
	globalFM348 = np.empty((0,6381))
	globalFM349 = np.empty((0,6381))
	globalFM350 = np.empty((0,6381))
	globalFM351 = np.empty((0,6381))
	globalFM352 = np.empty((0,6381))
	globalFM353 = np.empty((0,6381))
	globalFM354 = np.empty((0,6381))
	globalFM355 = np.empty((0,6381))
	globalFM356 = np.empty((0,6381))
	globalFM357 = np.empty((0,6381))
	globalFM358 = np.empty((0,6381))
	globalFM359 = np.empty((0,6381))
	globalFM360 = np.empty((0,6381))
	globalFM361 = np.empty((0,6381))
	globalFM362 = np.empty((0,6381))
	globalFM363 = np.empty((0,6381))
	globalFM364 = np.empty((0,6381))
	globalFM365 = np.empty((0,6381))
	globalFM366 = np.empty((0,6381))
	globalFM367 = np.empty((0,6381))
	globalFM368 = np.empty((0,6381))
	globalFM369 = np.empty((0,6381))
	globalFM370 = np.empty((0,6381))
	globalFM371 = np.empty((0,6381))
	globalFM372 = np.empty((0,6381))
	globalFM373 = np.empty((0,6381))
	globalFM374 = np.empty((0,6381))
	globalFM375 = np.empty((0,6381))
	globalFM376 = np.empty((0,6381))
	globalFM377 = np.empty((0,6381))
	globalFM378 = np.empty((0,6381))
	globalFM379 = np.empty((0,6381))
	globalFM380 = np.empty((0,6381))
	globalFM381 = np.empty((0,6381))
	globalFM382 = np.empty((0,6381))
	globalFM383 = np.empty((0,6381))
	globalFM384 = np.empty((0,6381))
	globalFM385 = np.empty((0,6381))
	globalFM386 = np.empty((0,6381))
	globalFM387 = np.empty((0,6381))
	globalFM388 = np.empty((0,6381))
	globalFM389 = np.empty((0,6381))
	globalFM390 = np.empty((0,6381))
	globalFM391 = np.empty((0,6381))
	globalFM392 = np.empty((0,6381))
	globalFM393 = np.empty((0,6381))
	globalFM394 = np.empty((0,6381))
	globalFM395 = np.empty((0,6381))
	globalFM396 = np.empty((0,6381))
	globalFM397 = np.empty((0,6381))
	globalFM398 = np.empty((0,6381))
	globalFM399 = np.empty((0,6381))
	globalFM400 = np.empty((0,6381))
	globalFM401 = np.empty((0,6381))
	globalFM402 = np.empty((0,6381))
	globalFM403 = np.empty((0,6381))
	globalFM404 = np.empty((0,6381))
	globalFM405 = np.empty((0,6381))
	globalFM406 = np.empty((0,6381))
	globalFM407 = np.empty((0,6381))
	globalFM408 = np.empty((0,6381))
	globalFM409 = np.empty((0,6381))
	globalFM410 = np.empty((0,6381))
	globalFM411 = np.empty((0,6381))
	globalFM412 = np.empty((0,6381))
	globalFM413 = np.empty((0,6381))
	globalFM414 = np.empty((0,6381))
	globalFM415 = np.empty((0,6381))
	globalFM416 = np.empty((0,6381))
	globalFM417 = np.empty((0,6381))
	globalFM418 = np.empty((0,6381))
	globalFM419 = np.empty((0,6381))
	globalFM420 = np.empty((0,6381))
	globalFM421 = np.empty((0,6381))
	globalFM422 = np.empty((0,6381))
	globalFM423 = np.empty((0,6381))
	globalFM424 = np.empty((0,6381))
	globalFM425 = np.empty((0,6381))
	globalFM426 = np.empty((0,6381))
	globalFM427 = np.empty((0,6381))
	globalFM428 = np.empty((0,6381))
	globalFM429 = np.empty((0,6381))
	globalFM430 = np.empty((0,6381))
	globalFM431 = np.empty((0,6381))
	globalFM432 = np.empty((0,6381))
	globalFM433 = np.empty((0,6381))
	globalFM434 = np.empty((0,6381))
	globalFM435 = np.empty((0,6381))
	globalFM436 = np.empty((0,6381))
	globalFM437 = np.empty((0,6381))
	globalFM438 = np.empty((0,6381))
	globalFM439 = np.empty((0,6381))
	globalFM440 = np.empty((0,6381))
	globalFM441 = np.empty((0,6381))
	globalFM442 = np.empty((0,6381))
	globalFM443 = np.empty((0,6381))
	globalFM444 = np.empty((0,6381))
	globalFM445 = np.empty((0,6381))
	globalFM446 = np.empty((0,6381))
	globalFM447 = np.empty((0,6381))
	globalFM448 = np.empty((0,6381))
	globalFM449 = np.empty((0,6381))
	globalFM450 = np.empty((0,6381))
	globalFM451 = np.empty((0,6381))
	globalFM452 = np.empty((0,6381))
	globalFM453 = np.empty((0,6381))
	globalFM454 = np.empty((0,6381))
	globalFM455 = np.empty((0,6381))
	globalFM456 = np.empty((0,6381))
	globalFM457 = np.empty((0,6381))
	globalFM458 = np.empty((0,6381))
	globalFM459 = np.empty((0,6381))
	globalFM460 = np.empty((0,6381))
	globalFM461 = np.empty((0,6381))
	globalFM462 = np.empty((0,6381))
	globalFM463 = np.empty((0,6381))
	globalFM464 = np.empty((0,6381))
	globalFM465 = np.empty((0,6381))
	globalFM466 = np.empty((0,6381))
	globalFM467 = np.empty((0,6381))
	globalFM468 = np.empty((0,6381))
	globalFM469 = np.empty((0,6381))
	globalFM470 = np.empty((0,6381))
	globalFM471 = np.empty((0,6381))
	globalFM472 = np.empty((0,6381))
	globalFM473 = np.empty((0,6381))
	globalFM474 = np.empty((0,6381))
	globalFM475 = np.empty((0,6381))
	globalFM476 = np.empty((0,6381))
	globalFM477 = np.empty((0,6381))
	globalFM478 = np.empty((0,6381))
	globalFM479 = np.empty((0,6381))
	globalFM480 = np.empty((0,6381))
	globalFM481 = np.empty((0,6381))
	globalFM482 = np.empty((0,6381))
	globalFM483 = np.empty((0,6381))
	globalFM484 = np.empty((0,6381))
	globalFM485 = np.empty((0,6381))
	globalFM486 = np.empty((0,6381))
	globalFM487 = np.empty((0,6381))
	globalFM488 = np.empty((0,6381))
	globalFM489 = np.empty((0,6381))
	globalFM490 = np.empty((0,6381))
	globalFM491 = np.empty((0,6381))
	globalFM492 = np.empty((0,6381))
	globalFM493 = np.empty((0,6381))
	globalFM494 = np.empty((0,6381))
	globalFM495 = np.empty((0,6381))
	globalFM496 = np.empty((0,6381))
	globalFM497 = np.empty((0,6381))
	globalFM498 = np.empty((0,6381))
	globalFM499 = np.empty((0,6381))
	globalFM500 = np.empty((0,6381))
	globalFM501 = np.empty((0,6381))
	globalFM502 = np.empty((0,6381))
	globalFM503 = np.empty((0,6381))
	globalFM504 = np.empty((0,6381))
	globalFM505 = np.empty((0,6381))
	globalFM506 = np.empty((0,6381))
	globalFM507 = np.empty((0,6381))
	globalFM508 = np.empty((0,6381))
	globalFM509 = np.empty((0,6381))
	globalFM510 = np.empty((0,6381))
	globalFM511 = np.empty((0,6381))
	globalFM512 = np.empty((0,6381))
	globalFM513 = np.empty((0,6381))
	globalFM514 = np.empty((0,6381))
	globalFM515 = np.empty((0,6381))
	globalFM516 = np.empty((0,6381))
	globalFM517 = np.empty((0,6381))
	globalFM518 = np.empty((0,6381))
	globalFM519 = np.empty((0,6381))
	globalFM520 = np.empty((0,6381))
	globalFM521 = np.empty((0,6381))
	globalFM522 = np.empty((0,6381))
	globalFM523 = np.empty((0,6381))
	globalFM524 = np.empty((0,6381))
	globalFM525 = np.empty((0,6381))
	globalFM526 = np.empty((0,6381))
	globalFM527 = np.empty((0,6381))
	globalFM528 = np.empty((0,6381))
	globalFM529 = np.empty((0,6381))
	globalFM530 = np.empty((0,6381))
	globalFM531 = np.empty((0,6381))
	globalFM532 = np.empty((0,6381))
	globalFM533 = np.empty((0,6381))
	globalFM534 = np.empty((0,6381))
	globalFM535 = np.empty((0,6381))
	globalFM536 = np.empty((0,6381))
	globalFM537 = np.empty((0,6381))
	globalFM538 = np.empty((0,6381))
	globalFM539 = np.empty((0,6381))
	globalFM540 = np.empty((0,6381))
	globalFM541 = np.empty((0,6381))
	globalFM542 = np.empty((0,6381))
	globalFM543 = np.empty((0,6381))
	globalFM544 = np.empty((0,6381))
	globalFM545 = np.empty((0,6381))
	globalFM546 = np.empty((0,6381))
	globalFM547 = np.empty((0,6381))
	globalFM548 = np.empty((0,6381))
	globalFM549 = np.empty((0,6381))
	globalFM550 = np.empty((0,6381))
	globalFM551 = np.empty((0,6381))
	globalFM552 = np.empty((0,6381))
	globalFM553 = np.empty((0,6381))
	globalFM554 = np.empty((0,6381))
	globalFM555 = np.empty((0,6381))
	globalFM556 = np.empty((0,6381))
	globalFM557 = np.empty((0,6381))
	globalFM558 = np.empty((0,6381))
	globalFM559 = np.empty((0,6381))
	globalFM560 = np.empty((0,6381))
	globalFM561 = np.empty((0,6381))
	globalFM562 = np.empty((0,6381))
	globalFM563 = np.empty((0,6381))
	globalFM564 = np.empty((0,6381))
	globalFM565 = np.empty((0,6381))
	globalFM566 = np.empty((0,6381))
	globalFM567 = np.empty((0,6381))
	globalFM568 = np.empty((0,6381))
	globalFM569 = np.empty((0,6381))
	globalFM570 = np.empty((0,6381))
	globalFM571 = np.empty((0,6381))
	globalFM572 = np.empty((0,6381))
	globalFM573 = np.empty((0,6381))
	globalFM574 = np.empty((0,6381))
	globalFM575 = np.empty((0,6381))
	globalFM576 = np.empty((0,6381))
	globalFM577 = np.empty((0,6381))
	globalFM578 = np.empty((0,6381))
	globalFM579 = np.empty((0,6381))
	globalFM580 = np.empty((0,6381))
	globalFM581 = np.empty((0,6381))
	globalFM582 = np.empty((0,6381))
	globalFM583 = np.empty((0,6381))
	globalFM584 = np.empty((0,6381))
	globalFM585 = np.empty((0,6381))
	globalFM586 = np.empty((0,6381))
	globalFM587 = np.empty((0,6381))
	globalFM588 = np.empty((0,6381))
	globalFM589 = np.empty((0,6381))
	globalFM590 = np.empty((0,6381))
	globalFM591 = np.empty((0,6381))
	globalFM592 = np.empty((0,6381))
	globalFM593 = np.empty((0,6381))
	globalFM594 = np.empty((0,6381))
	globalFM595 = np.empty((0,6381))
	globalFM596 = np.empty((0,6381))
	globalFM597 = np.empty((0,6381))
	globalFM598 = np.empty((0,6381))
	globalFM599 = np.empty((0,6381))
	globalFM600 = np.empty((0,6381))
	globalFM601 = np.empty((0,6381))
	globalFM602 = np.empty((0,6381))
	globalFM603 = np.empty((0,6381))
	globalFM604 = np.empty((0,6381))
	globalFM605 = np.empty((0,6381))
	globalFM606 = np.empty((0,6381))
	globalFM607 = np.empty((0,6381))
	globalFM608 = np.empty((0,6381))
	globalFM609 = np.empty((0,6381))
	globalFM610 = np.empty((0,6381))
	globalFM611 = np.empty((0,6381))
	globalFM612 = np.empty((0,6381))
	globalFM613 = np.empty((0,6381))
	globalFM614 = np.empty((0,6381))
	globalFM615 = np.empty((0,6381))
	globalFM616 = np.empty((0,6381))
	globalFM617 = np.empty((0,6381))
	globalFM618 = np.empty((0,6381))
	globalFM619 = np.empty((0,6381))
	globalFM620 = np.empty((0,6381))
	globalFM621 = np.empty((0,6381))
	globalFM622 = np.empty((0,6381))
	globalFM623 = np.empty((0,6381))
	globalFM624 = np.empty((0,6381))
	globalFM625 = np.empty((0,6381))
	globalFM626 = np.empty((0,6381))
	globalFM627 = np.empty((0,6381))
	globalFM628 = np.empty((0,6381))
	globalFM629 = np.empty((0,6381))
	globalFM630 = np.empty((0,6381))
	globalFM631 = np.empty((0,6381))
	globalFM632 = np.empty((0,6381))
	globalFM633 = np.empty((0,6381))
	globalFM634 = np.empty((0,6381))
	globalFM635 = np.empty((0,6381))
	globalFM636 = np.empty((0,6381))
	globalFM637 = np.empty((0,6381))
	globalFM638 = np.empty((0,6381))
	globalFM639 = np.empty((0,6381))
	globalFM640 = np.empty((0,6381))
	globalFM641 = np.empty((0,6381))
	globalFM642 = np.empty((0,6381))
	globalFM643 = np.empty((0,6381))
	globalFM644 = np.empty((0,6381))
	globalFM645 = np.empty((0,6381))
	globalFM646 = np.empty((0,6381))
	globalFM647 = np.empty((0,6381))
	globalFM648 = np.empty((0,6381))
	globalFM649 = np.empty((0,6381))
	globalFM650 = np.empty((0,6381))
	globalFM651 = np.empty((0,6381))
	globalFM652 = np.empty((0,6381))
	globalFM653 = np.empty((0,6381))
	globalFM654 = np.empty((0,6381))
	globalFM655 = np.empty((0,6381))
	globalFM656 = np.empty((0,6381))
	globalFM657 = np.empty((0,6381))
	globalFM658 = np.empty((0,6381))
	globalFM659 = np.empty((0,6381))
	globalFM660 = np.empty((0,6381))
	globalFM661 = np.empty((0,6381))
	globalFM662 = np.empty((0,6381))
	globalFM663 = np.empty((0,6381))
	globalFM664 = np.empty((0,6381))
	globalFM665 = np.empty((0,6381))
	globalFM666 = np.empty((0,6381))
	globalFM667 = np.empty((0,6381))
	globalFM668 = np.empty((0,6381))
	globalFM669 = np.empty((0,6381))
	globalFM670 = np.empty((0,6381))
	globalFM671 = np.empty((0,6381))
	globalFM672 = np.empty((0,6381))
	globalFM673 = np.empty((0,6381))
	globalFM674 = np.empty((0,6381))
	globalFM675 = np.empty((0,6381))
	globalFM676 = np.empty((0,6381))
	globalFM677 = np.empty((0,6381))
	globalFM678 = np.empty((0,6381))
	globalFM679 = np.empty((0,6381))
	globalFM680 = np.empty((0,6381))
	globalFM681 = np.empty((0,6381))
	globalFM682 = np.empty((0,6381))
	globalFM683 = np.empty((0,6381))
	globalFM684 = np.empty((0,6381))
	globalFM685 = np.empty((0,6381))
	globalFM686 = np.empty((0,6381))
	globalFM687 = np.empty((0,6381))
	globalFM688 = np.empty((0,6381))
	globalFM689 = np.empty((0,6381))
	globalFM690 = np.empty((0,6381))
	globalFM691 = np.empty((0,6381))
	globalFM692 = np.empty((0,6381))
	globalFM693 = np.empty((0,6381))
	globalFM694 = np.empty((0,6381))
	globalFM695 = np.empty((0,6381))
	globalFM696 = np.empty((0,6381))
	globalFM697 = np.empty((0,6381))
	globalFM698 = np.empty((0,6381))
	globalFM699 = np.empty((0,6381))
	globalFM700 = np.empty((0,6381))
	globalFM701 = np.empty((0,6381))
	globalFM702 = np.empty((0,6381))
	globalFM703 = np.empty((0,6381))
	globalFM704 = np.empty((0,6381))
	globalFM705 = np.empty((0,6381))
	globalFM706 = np.empty((0,6381))
	globalFM707 = np.empty((0,6381))
	globalFM708 = np.empty((0,6381))
	globalFM709 = np.empty((0,6381))
	globalFM710 = np.empty((0,6381))
	globalFM711 = np.empty((0,6381))
	globalFM712 = np.empty((0,6381))
	globalFM713 = np.empty((0,6381))
	globalFM714 = np.empty((0,6381))
	globalFM715 = np.empty((0,6381))
	globalFM716 = np.empty((0,6381))
	globalFM717 = np.empty((0,6381))
	globalFM718 = np.empty((0,6381))
	globalFM719 = np.empty((0,6381))
	globalFM720 = np.empty((0,6381))
	globalFM721 = np.empty((0,6381))
	globalFM722 = np.empty((0,6381))
	globalFM723 = np.empty((0,6381))
	globalFM724 = np.empty((0,6381))
	globalFM725 = np.empty((0,6381))
	globalFM726 = np.empty((0,6381))
	globalFM727 = np.empty((0,6381))
	globalFM728 = np.empty((0,6381))
	globalFM729 = np.empty((0,6381))
	globalFM730 = np.empty((0,6381))
	globalFM731 = np.empty((0,6381))
	globalFM732 = np.empty((0,6381))
	globalFM733 = np.empty((0,6381))
	globalFM734 = np.empty((0,6381))
	globalFM735 = np.empty((0,6381))
	globalFM736 = np.empty((0,6381))
	globalFM737 = np.empty((0,6381))
	globalFM738 = np.empty((0,6381))
	globalFM739 = np.empty((0,6381))
	globalFM740 = np.empty((0,6381))
	globalFM741 = np.empty((0,6381))
	globalFM742 = np.empty((0,6381))
	globalFM743 = np.empty((0,6381))
	globalFM744 = np.empty((0,6381))
	globalFM745 = np.empty((0,6381))
	globalFM746 = np.empty((0,6381))
	globalFM747 = np.empty((0,6381))
	globalFM748 = np.empty((0,6381))
	globalFM749 = np.empty((0,6381))
	globalFM750 = np.empty((0,6381))
	globalFM751 = np.empty((0,6381))
	globalFM752 = np.empty((0,6381))
	globalFM753 = np.empty((0,6381))
	globalFM754 = np.empty((0,6381))
	globalFM755 = np.empty((0,6381))
	globalFM756 = np.empty((0,6381))
	globalFM757 = np.empty((0,6381))
	globalFM758 = np.empty((0,6381))
	globalFM759 = np.empty((0,6381))
	globalFM760 = np.empty((0,6381))
	globalFM761 = np.empty((0,6381))
	globalFM762 = np.empty((0,6381))
	globalFM763 = np.empty((0,6381))
	globalFM764 = np.empty((0,6381))
	globalFM765 = np.empty((0,6381))
	globalFM766 = np.empty((0,6381))
	globalFM767 = np.empty((0,6381))
	globalFM768 = np.empty((0,6381))
	globalFM769 = np.empty((0,6381))
	globalFM770 = np.empty((0,6381))
	globalFM771 = np.empty((0,6381))
	globalFM772 = np.empty((0,6381))
	globalFM773 = np.empty((0,6381))
	globalFM774 = np.empty((0,6381))
	globalFM775 = np.empty((0,6381))
	globalFM776 = np.empty((0,6381))
	globalFM777 = np.empty((0,6381))
	globalFM778 = np.empty((0,6381))
	globalFM779 = np.empty((0,6381))
	globalFM780 = np.empty((0,6381))
	globalFM781 = np.empty((0,6381))
	globalFM782 = np.empty((0,6381))
	globalFM783 = np.empty((0,6381))
	globalFM784 = np.empty((0,6381))
	globalFM785 = np.empty((0,6381))
	globalFM786 = np.empty((0,6381))
	globalFM787 = np.empty((0,6381))
	globalFM788 = np.empty((0,6381))
	globalFM789 = np.empty((0,6381))
	globalFM790 = np.empty((0,6381))
	globalFM791 = np.empty((0,6381))
	globalFM792 = np.empty((0,6381))
	globalFM793 = np.empty((0,6381))
	globalFM794 = np.empty((0,6381))
	globalFM795 = np.empty((0,6381))
	globalFM796 = np.empty((0,6381))
	globalFM797 = np.empty((0,6381))
	globalFM798 = np.empty((0,6381))
	globalFM799 = np.empty((0,6381))
	globalFM800 = np.empty((0,6381))
	globalFM801 = np.empty((0,6381))
	globalFM802 = np.empty((0,6381))
	globalFM803 = np.empty((0,6381))
	globalFM804 = np.empty((0,6381))
	globalFM805 = np.empty((0,6381))
	globalFM806 = np.empty((0,6381))
	globalFM807 = np.empty((0,6381))
	globalFM808 = np.empty((0,6381))
	globalFM809 = np.empty((0,6381))
	globalFM810 = np.empty((0,6381))
	globalFM811 = np.empty((0,6381))
	globalFM812 = np.empty((0,6381))
	globalFM813 = np.empty((0,6381))
	globalFM814 = np.empty((0,6381))
	globalFM815 = np.empty((0,6381))
	globalFM816 = np.empty((0,6381))
	globalFM817 = np.empty((0,6381))
	globalFM818 = np.empty((0,6381))
	globalFM819 = np.empty((0,6381))
	globalFM820 = np.empty((0,6381))
	globalFM821 = np.empty((0,6381))
	globalFM822 = np.empty((0,6381))
	globalFM823 = np.empty((0,6381))
	globalFM824 = np.empty((0,6381))
	globalFM825 = np.empty((0,6381))
	globalFM826 = np.empty((0,6381))
	globalFM827 = np.empty((0,6381))
	globalFM828 = np.empty((0,6381))
	globalFM829 = np.empty((0,6381))
	globalFM830 = np.empty((0,6381))
	globalFM831 = np.empty((0,6381))
	globalFM832 = np.empty((0,6381))
	globalFM833 = np.empty((0,6381))
	globalFM834 = np.empty((0,6381))
	globalFM835 = np.empty((0,6381))
	globalFM836 = np.empty((0,6381))
	globalFM837 = np.empty((0,6381))
	globalFM838 = np.empty((0,6381))
	globalFM839 = np.empty((0,6381))
	globalFM840 = np.empty((0,6381))
	globalFM841 = np.empty((0,6381))
	globalFM842 = np.empty((0,6381))
	globalFM843 = np.empty((0,6381))
	globalFM844 = np.empty((0,6381))
	globalFM845 = np.empty((0,6381))
	globalFM846 = np.empty((0,6381))
	globalFM847 = np.empty((0,6381))
	globalFM848 = np.empty((0,6381))
	globalFM849 = np.empty((0,6381))
	globalFM850 = np.empty((0,6381))
	globalFM851 = np.empty((0,6381))
	globalFM852 = np.empty((0,6381))
	globalFM853 = np.empty((0,6381))
	globalFM854 = np.empty((0,6381))
	globalFM855 = np.empty((0,6381))
	globalFM856 = np.empty((0,6381))
	globalFM857 = np.empty((0,6381))
	globalFM858 = np.empty((0,6381))
	globalFM859 = np.empty((0,6381))
	globalFM860 = np.empty((0,6381))
	globalFM861 = np.empty((0,6381))
	globalFM862 = np.empty((0,6381))
	globalFM863 = np.empty((0,6381))
	globalFM864 = np.empty((0,6381))
	globalFM865 = np.empty((0,6381))
	globalFM866 = np.empty((0,6381))
	globalFM867 = np.empty((0,6381))
	globalFM868 = np.empty((0,6381))
	globalFM869 = np.empty((0,6381))
	globalFM870 = np.empty((0,6381))
	globalFM871 = np.empty((0,6381))
	globalFM872 = np.empty((0,6381))
	globalFM873 = np.empty((0,6381))
	globalFM874 = np.empty((0,6381))
	globalFM875 = np.empty((0,6381))
	globalFM876 = np.empty((0,6381))
	globalFM877 = np.empty((0,6381))
	globalFM878 = np.empty((0,6381))
	globalFM879 = np.empty((0,6381))
	globalFM880 = np.empty((0,6381))
	globalFM881 = np.empty((0,6381))
	globalFM882 = np.empty((0,6381))
	globalFM883 = np.empty((0,6381))
	globalFM884 = np.empty((0,6381))
	globalFM885 = np.empty((0,6381))
	globalFM886 = np.empty((0,6381))
	globalFM887 = np.empty((0,6381))
	globalFM888 = np.empty((0,6381))
	globalFM889 = np.empty((0,6381))
	globalFM890 = np.empty((0,6381))
	globalFM891 = np.empty((0,6381))
	globalFM892 = np.empty((0,6381))
	globalFM893 = np.empty((0,6381))
	globalFM894 = np.empty((0,6381))
	globalFM895 = np.empty((0,6381))
	globalFM896 = np.empty((0,6381))
	globalFM897 = np.empty((0,6381))
	globalFM898 = np.empty((0,6381))
	globalFM899 = np.empty((0,6381))
	globalFM900 = np.empty((0,6381))
	globalFM901 = np.empty((0,6381))
	globalFM902 = np.empty((0,6381))
	globalFM903 = np.empty((0,6381))
	globalFM904 = np.empty((0,6381))
	globalFM905 = np.empty((0,6381))
	globalFM906 = np.empty((0,6381))
	globalFM907 = np.empty((0,6381))
	globalFM908 = np.empty((0,6381))
	globalFM909 = np.empty((0,6381))
	globalFM910 = np.empty((0,6381))
	globalFM911 = np.empty((0,6381))
	globalFM912 = np.empty((0,6381))
	globalFM913 = np.empty((0,6381))
	globalFM914 = np.empty((0,6381))
	globalFM915 = np.empty((0,6381))
	globalFM916 = np.empty((0,6381))
	globalFM917 = np.empty((0,6381))
	globalFM918 = np.empty((0,6381))
	globalFM919 = np.empty((0,6381))
	globalFM920 = np.empty((0,6381))
	globalFM921 = np.empty((0,6381))
	globalFM922 = np.empty((0,6381))
	globalFM923 = np.empty((0,6381))
	globalFM924 = np.empty((0,6381))
	globalFM925 = np.empty((0,6381))
	globalFM926 = np.empty((0,6381))
	globalFM927 = np.empty((0,6381))
	globalFM928 = np.empty((0,6381))
	globalFM929 = np.empty((0,6381))
	globalFM930 = np.empty((0,6381))
	globalFM931 = np.empty((0,6381))
	globalFM932 = np.empty((0,6381))
	globalFM933 = np.empty((0,6381))
	globalFM934 = np.empty((0,6381))
	globalFM935 = np.empty((0,6381))
	globalFM936 = np.empty((0,6381))
	globalFM937 = np.empty((0,6381))
	globalFM938 = np.empty((0,6381))
	globalFM939 = np.empty((0,6381))
	globalFM940 = np.empty((0,6381))
	globalFM941 = np.empty((0,6381))
	globalFM942 = np.empty((0,6381))
	globalFM943 = np.empty((0,6381))
	globalFM944 = np.empty((0,6381))
	globalFM945 = np.empty((0,6381))
	globalFM946 = np.empty((0,6381))
	globalFM947 = np.empty((0,6381))
	globalFM948 = np.empty((0,6381))
	globalFM949 = np.empty((0,6381))
	globalFM950 = np.empty((0,6381))
	globalFM951 = np.empty((0,6381))
	globalFM952 = np.empty((0,6381))
	globalFM953 = np.empty((0,6381))
	globalFM954 = np.empty((0,6381))
	globalFM955 = np.empty((0,6381))
	globalFM956 = np.empty((0,6381))
	globalFM957 = np.empty((0,6381))
	globalFM958 = np.empty((0,6381))
	globalFM959 = np.empty((0,6381))
	globalFM960 = np.empty((0,6381))
	globalFM961 = np.empty((0,6381))
	globalFM962 = np.empty((0,6381))
	globalFM963 = np.empty((0,6381))
	globalFM964 = np.empty((0,6381))
	globalFM965 = np.empty((0,6381))
	globalFM966 = np.empty((0,6381))
	globalFM967 = np.empty((0,6381))
	globalFM968 = np.empty((0,6381))
	globalFM969 = np.empty((0,6381))
	globalFM970 = np.empty((0,6381))
	globalFM971 = np.empty((0,6381))
	globalFM972 = np.empty((0,6381))
	globalFM973 = np.empty((0,6381))
	globalFM974 = np.empty((0,6381))
	globalFM975 = np.empty((0,6381))
	globalFM976 = np.empty((0,6381))
	globalFM977 = np.empty((0,6381))
	globalFM978 = np.empty((0,6381))
	globalFM979 = np.empty((0,6381))
	globalFM980 = np.empty((0,6381))
	globalFM981 = np.empty((0,6381))
	globalFM982 = np.empty((0,6381))
	globalFM983 = np.empty((0,6381))
	globalFM984 = np.empty((0,6381))
	globalFM985 = np.empty((0,6381))
	globalFM986 = np.empty((0,6381))
	globalFM987 = np.empty((0,6381))
	globalFM988 = np.empty((0,6381))
	globalFM989 = np.empty((0,6381))
	globalFM990 = np.empty((0,6381))
	globalFM991 = np.empty((0,6381))
	globalFM992 = np.empty((0,6381))
	globalFM993 = np.empty((0,6381))
	globalFM994 = np.empty((0,6381))
	globalFM995 = np.empty((0,6381))
	globalFM996 = np.empty((0,6381))
	globalFM997 = np.empty((0,6381))
	globalFM998 = np.empty((0,6381))
	globalFM999 = np.empty((0,6381))

	M = 0

	for dict in dictsList[0*int(length/numero):1*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM0 = np.row_stack((globalFM0,dataArray))
		M += 1
	print(M)

	for dict in dictsList[1*int(length/numero):2*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM1 = np.row_stack((globalFM1,dataArray))
		M += 1
	print(M)

	for dict in dictsList[2*int(length/numero):3*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM2 = np.row_stack((globalFM2,dataArray))
		M += 1
	print(M)

	for dict in dictsList[3*int(length/numero):4*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM3 = np.row_stack((globalFM3,dataArray))
		M += 1
	print(M)

	for dict in dictsList[4*int(length/numero):5*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM4 = np.row_stack((globalFM4,dataArray))
		M += 1
	print(M)

	for dict in dictsList[5*int(length/numero):6*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM5 = np.row_stack((globalFM5,dataArray))
		M += 1
	print(M)

	for dict in dictsList[6*int(length/numero):7*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM6 = np.row_stack((globalFM6,dataArray))
		M += 1
	print(M)

	for dict in dictsList[7*int(length/numero):8*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM7 = np.row_stack((globalFM7,dataArray))
		M += 1
	print(M)

	for dict in dictsList[8*int(length/numero):9*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM8 = np.row_stack((globalFM8,dataArray))
		M += 1
	print(M)

	for dict in dictsList[9*int(length/numero):10*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM9 = np.row_stack((globalFM9,dataArray))
		M += 1
	print(M)

	for dict in dictsList[10*int(length/numero):11*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM10 = np.row_stack((globalFM10,dataArray))
		M += 1
	print(M)

	for dict in dictsList[11*int(length/numero):12*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM11 = np.row_stack((globalFM11,dataArray))
		M += 1
	print(M)

	for dict in dictsList[12*int(length/numero):13*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM12 = np.row_stack((globalFM12,dataArray))
		M += 1
	print(M)

	for dict in dictsList[13*int(length/numero):14*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM13 = np.row_stack((globalFM13,dataArray))
		M += 1
	print(M)

	for dict in dictsList[14*int(length/numero):15*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM14 = np.row_stack((globalFM14,dataArray))
		M += 1
	print(M)

	for dict in dictsList[15*int(length/numero):16*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM15 = np.row_stack((globalFM15,dataArray))
		M += 1
	print(M)

	for dict in dictsList[16*int(length/numero):17*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM16 = np.row_stack((globalFM16,dataArray))
		M += 1
	print(M)

	for dict in dictsList[17*int(length/numero):18*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM17 = np.row_stack((globalFM17,dataArray))
		M += 1
	print(M)

	for dict in dictsList[18*int(length/numero):19*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM18 = np.row_stack((globalFM18,dataArray))
		M += 1
	print(M)

	for dict in dictsList[19*int(length/numero):20*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM19 = np.row_stack((globalFM19,dataArray))
		M += 1
	print(M)

	for dict in dictsList[20*int(length/numero):21*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM20 = np.row_stack((globalFM20,dataArray))
		M += 1
	print(M)

	for dict in dictsList[21*int(length/numero):22*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM21 = np.row_stack((globalFM21,dataArray))
		M += 1
	print(M)

	for dict in dictsList[22*int(length/numero):23*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM22 = np.row_stack((globalFM22,dataArray))
		M += 1
	print(M)

	for dict in dictsList[23*int(length/numero):24*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM23 = np.row_stack((globalFM23,dataArray))
		M += 1
	print(M)

	for dict in dictsList[24*int(length/numero):25*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM24 = np.row_stack((globalFM24,dataArray))
		M += 1
	print(M)

	for dict in dictsList[25*int(length/numero):26*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM25 = np.row_stack((globalFM25,dataArray))
		M += 1
	print(M)

	for dict in dictsList[26*int(length/numero):27*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM26 = np.row_stack((globalFM26,dataArray))
		M += 1
	print(M)

	for dict in dictsList[27*int(length/numero):28*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM27 = np.row_stack((globalFM27,dataArray))
		M += 1
	print(M)

	for dict in dictsList[28*int(length/numero):29*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM28 = np.row_stack((globalFM28,dataArray))
		M += 1
	print(M)

	for dict in dictsList[29*int(length/numero):30*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM29 = np.row_stack((globalFM29,dataArray))
		M += 1
	print(M)

	for dict in dictsList[30*int(length/numero):31*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM30 = np.row_stack((globalFM30,dataArray))
		M += 1
	print(M)

	for dict in dictsList[31*int(length/numero):32*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM31 = np.row_stack((globalFM31,dataArray))
		M += 1
	print(M)

	for dict in dictsList[32*int(length/numero):33*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM32 = np.row_stack((globalFM32,dataArray))
		M += 1
	print(M)

	for dict in dictsList[33*int(length/numero):34*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM33 = np.row_stack((globalFM33,dataArray))
		M += 1
	print(M)

	for dict in dictsList[34*int(length/numero):35*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM34 = np.row_stack((globalFM34,dataArray))
		M += 1
	print(M)

	for dict in dictsList[35*int(length/numero):36*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM35 = np.row_stack((globalFM35,dataArray))
		M += 1
	print(M)

	for dict in dictsList[36*int(length/numero):37*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM36 = np.row_stack((globalFM36,dataArray))
		M += 1
	print(M)

	for dict in dictsList[37*int(length/numero):38*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM37 = np.row_stack((globalFM37,dataArray))
		M += 1
	print(M)

	for dict in dictsList[38*int(length/numero):39*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM38 = np.row_stack((globalFM38,dataArray))
		M += 1
	print(M)

	for dict in dictsList[39*int(length/numero):40*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM39 = np.row_stack((globalFM39,dataArray))
		M += 1
	print(M)

	for dict in dictsList[40*int(length/numero):41*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM40 = np.row_stack((globalFM40,dataArray))
		M += 1
	print(M)

	for dict in dictsList[41*int(length/numero):42*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM41 = np.row_stack((globalFM41,dataArray))
		M += 1
	print(M)

	for dict in dictsList[42*int(length/numero):43*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM42 = np.row_stack((globalFM42,dataArray))
		M += 1
	print(M)

	for dict in dictsList[43*int(length/numero):44*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM43 = np.row_stack((globalFM43,dataArray))
		M += 1
	print(M)

	for dict in dictsList[44*int(length/numero):45*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM44 = np.row_stack((globalFM44,dataArray))
		M += 1
	print(M)

	for dict in dictsList[45*int(length/numero):46*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM45 = np.row_stack((globalFM45,dataArray))
		M += 1
	print(M)

	for dict in dictsList[46*int(length/numero):47*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM46 = np.row_stack((globalFM46,dataArray))
		M += 1
	print(M)

	for dict in dictsList[47*int(length/numero):48*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM47 = np.row_stack((globalFM47,dataArray))
		M += 1
	print(M)

	for dict in dictsList[48*int(length/numero):49*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM48 = np.row_stack((globalFM48,dataArray))
		M += 1
	print(M)

	for dict in dictsList[49*int(length/numero):50*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM49 = np.row_stack((globalFM49,dataArray))
		M += 1
	print(M)

	for dict in dictsList[50*int(length/numero):51*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM50 = np.row_stack((globalFM50,dataArray))
		M += 1
	print(M)

	for dict in dictsList[51*int(length/numero):52*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM51 = np.row_stack((globalFM51,dataArray))
		M += 1
	print(M)

	for dict in dictsList[52*int(length/numero):53*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM52 = np.row_stack((globalFM52,dataArray))
		M += 1
	print(M)

	for dict in dictsList[53*int(length/numero):54*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM53 = np.row_stack((globalFM53,dataArray))
		M += 1
	print(M)

	for dict in dictsList[54*int(length/numero):55*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM54 = np.row_stack((globalFM54,dataArray))
		M += 1
	print(M)

	for dict in dictsList[55*int(length/numero):56*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM55 = np.row_stack((globalFM55,dataArray))
		M += 1
	print(M)

	for dict in dictsList[56*int(length/numero):57*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM56 = np.row_stack((globalFM56,dataArray))
		M += 1
	print(M)

	for dict in dictsList[57*int(length/numero):58*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM57 = np.row_stack((globalFM57,dataArray))
		M += 1
	print(M)

	for dict in dictsList[58*int(length/numero):59*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM58 = np.row_stack((globalFM58,dataArray))
		M += 1
	print(M)

	for dict in dictsList[59*int(length/numero):60*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM59 = np.row_stack((globalFM59,dataArray))
		M += 1
	print(M)

	for dict in dictsList[60*int(length/numero):61*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM60 = np.row_stack((globalFM60,dataArray))
		M += 1
	print(M)

	for dict in dictsList[61*int(length/numero):62*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM61 = np.row_stack((globalFM61,dataArray))
		M += 1
	print(M)

	for dict in dictsList[62*int(length/numero):63*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM62 = np.row_stack((globalFM62,dataArray))
		M += 1
	print(M)

	for dict in dictsList[63*int(length/numero):64*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM63 = np.row_stack((globalFM63,dataArray))
		M += 1
	print(M)

	for dict in dictsList[64*int(length/numero):65*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM64 = np.row_stack((globalFM64,dataArray))
		M += 1
	print(M)

	for dict in dictsList[65*int(length/numero):66*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM65 = np.row_stack((globalFM65,dataArray))
		M += 1
	print(M)

	for dict in dictsList[66*int(length/numero):67*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM66 = np.row_stack((globalFM66,dataArray))
		M += 1
	print(M)

	for dict in dictsList[67*int(length/numero):68*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM67 = np.row_stack((globalFM67,dataArray))
		M += 1
	print(M)

	for dict in dictsList[68*int(length/numero):69*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM68 = np.row_stack((globalFM68,dataArray))
		M += 1
	print(M)

	for dict in dictsList[69*int(length/numero):70*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM69 = np.row_stack((globalFM69,dataArray))
		M += 1
	print(M)

	for dict in dictsList[70*int(length/numero):71*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM70 = np.row_stack((globalFM70,dataArray))
		M += 1
	print(M)

	for dict in dictsList[71*int(length/numero):72*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM71 = np.row_stack((globalFM71,dataArray))
		M += 1
	print(M)

	for dict in dictsList[72*int(length/numero):73*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM72 = np.row_stack((globalFM72,dataArray))
		M += 1
	print(M)

	for dict in dictsList[73*int(length/numero):74*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM73 = np.row_stack((globalFM73,dataArray))
		M += 1
	print(M)

	for dict in dictsList[74*int(length/numero):75*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM74 = np.row_stack((globalFM74,dataArray))
		M += 1
	print(M)

	for dict in dictsList[75*int(length/numero):76*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM75 = np.row_stack((globalFM75,dataArray))
		M += 1
	print(M)

	for dict in dictsList[76*int(length/numero):77*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM76 = np.row_stack((globalFM76,dataArray))
		M += 1
	print(M)

	for dict in dictsList[77*int(length/numero):78*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM77 = np.row_stack((globalFM77,dataArray))
		M += 1
	print(M)

	for dict in dictsList[78*int(length/numero):79*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM78 = np.row_stack((globalFM78,dataArray))
		M += 1
	print(M)

	for dict in dictsList[79*int(length/numero):80*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM79 = np.row_stack((globalFM79,dataArray))
		M += 1
	print(M)

	for dict in dictsList[80*int(length/numero):81*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM80 = np.row_stack((globalFM80,dataArray))
		M += 1
	print(M)

	for dict in dictsList[81*int(length/numero):82*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM81 = np.row_stack((globalFM81,dataArray))
		M += 1
	print(M)

	for dict in dictsList[82*int(length/numero):83*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM82 = np.row_stack((globalFM82,dataArray))
		M += 1
	print(M)

	for dict in dictsList[83*int(length/numero):84*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM83 = np.row_stack((globalFM83,dataArray))
		M += 1
	print(M)

	for dict in dictsList[84*int(length/numero):85*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM84 = np.row_stack((globalFM84,dataArray))
		M += 1
	print(M)

	for dict in dictsList[85*int(length/numero):86*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM85 = np.row_stack((globalFM85,dataArray))
		M += 1
	print(M)

	for dict in dictsList[86*int(length/numero):87*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM86 = np.row_stack((globalFM86,dataArray))
		M += 1
	print(M)

	for dict in dictsList[87*int(length/numero):88*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM87 = np.row_stack((globalFM87,dataArray))
		M += 1
	print(M)

	for dict in dictsList[88*int(length/numero):89*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM88 = np.row_stack((globalFM88,dataArray))
		M += 1
	print(M)

	for dict in dictsList[89*int(length/numero):90*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM89 = np.row_stack((globalFM89,dataArray))
		M += 1
	print(M)

	for dict in dictsList[90*int(length/numero):91*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM90 = np.row_stack((globalFM90,dataArray))
		M += 1
	print(M)

	for dict in dictsList[91*int(length/numero):92*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM91 = np.row_stack((globalFM91,dataArray))
		M += 1
	print(M)

	for dict in dictsList[92*int(length/numero):93*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM92 = np.row_stack((globalFM92,dataArray))
		M += 1
	print(M)

	for dict in dictsList[93*int(length/numero):94*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM93 = np.row_stack((globalFM93,dataArray))
		M += 1
	print(M)

	for dict in dictsList[94*int(length/numero):95*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM94 = np.row_stack((globalFM94,dataArray))
		M += 1
	print(M)

	for dict in dictsList[95*int(length/numero):96*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM95 = np.row_stack((globalFM95,dataArray))
		M += 1
	print(M)

	for dict in dictsList[96*int(length/numero):97*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM96 = np.row_stack((globalFM96,dataArray))
		M += 1
	print(M)

	for dict in dictsList[97*int(length/numero):98*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM97 = np.row_stack((globalFM97,dataArray))
		M += 1
	print(M)

	for dict in dictsList[98*int(length/numero):99*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM98 = np.row_stack((globalFM98,dataArray))
		M += 1
	print(M)

	for dict in dictsList[99*int(length/numero):100*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM99 = np.row_stack((globalFM99,dataArray))
		M += 1
	print(M)

	for dict in dictsList[100*int(length/numero):101*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM100 = np.row_stack((globalFM100,dataArray))
		M += 1
	print(M)

	for dict in dictsList[101*int(length/numero):102*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM101 = np.row_stack((globalFM101,dataArray))
		M += 1
	print(M)

	for dict in dictsList[102*int(length/numero):103*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM102 = np.row_stack((globalFM102,dataArray))
		M += 1
	print(M)

	for dict in dictsList[103*int(length/numero):104*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM103 = np.row_stack((globalFM103,dataArray))
		M += 1
	print(M)

	for dict in dictsList[104*int(length/numero):105*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM104 = np.row_stack((globalFM104,dataArray))
		M += 1
	print(M)

	for dict in dictsList[105*int(length/numero):106*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM105 = np.row_stack((globalFM105,dataArray))
		M += 1
	print(M)

	for dict in dictsList[106*int(length/numero):107*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM106 = np.row_stack((globalFM106,dataArray))
		M += 1
	print(M)

	for dict in dictsList[107*int(length/numero):108*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM107 = np.row_stack((globalFM107,dataArray))
		M += 1
	print(M)

	for dict in dictsList[108*int(length/numero):109*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM108 = np.row_stack((globalFM108,dataArray))
		M += 1
	print(M)

	for dict in dictsList[109*int(length/numero):110*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM109 = np.row_stack((globalFM109,dataArray))
		M += 1
	print(M)

	for dict in dictsList[110*int(length/numero):111*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM110 = np.row_stack((globalFM110,dataArray))
		M += 1
	print(M)

	for dict in dictsList[111*int(length/numero):112*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM111 = np.row_stack((globalFM111,dataArray))
		M += 1
	print(M)

	for dict in dictsList[112*int(length/numero):113*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM112 = np.row_stack((globalFM112,dataArray))
		M += 1
	print(M)

	for dict in dictsList[113*int(length/numero):114*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM113 = np.row_stack((globalFM113,dataArray))
		M += 1
	print(M)

	for dict in dictsList[114*int(length/numero):115*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM114 = np.row_stack((globalFM114,dataArray))
		M += 1
	print(M)

	for dict in dictsList[115*int(length/numero):116*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM115 = np.row_stack((globalFM115,dataArray))
		M += 1
	print(M)

	for dict in dictsList[116*int(length/numero):117*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM116 = np.row_stack((globalFM116,dataArray))
		M += 1
	print(M)

	for dict in dictsList[117*int(length/numero):118*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM117 = np.row_stack((globalFM117,dataArray))
		M += 1
	print(M)

	for dict in dictsList[118*int(length/numero):119*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM118 = np.row_stack((globalFM118,dataArray))
		M += 1
	print(M)

	for dict in dictsList[119*int(length/numero):120*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM119 = np.row_stack((globalFM119,dataArray))
		M += 1
	print(M)

	for dict in dictsList[120*int(length/numero):121*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM120 = np.row_stack((globalFM120,dataArray))
		M += 1
	print(M)

	for dict in dictsList[121*int(length/numero):122*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM121 = np.row_stack((globalFM121,dataArray))
		M += 1
	print(M)

	for dict in dictsList[122*int(length/numero):123*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM122 = np.row_stack((globalFM122,dataArray))
		M += 1
	print(M)

	for dict in dictsList[123*int(length/numero):124*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM123 = np.row_stack((globalFM123,dataArray))
		M += 1
	print(M)

	for dict in dictsList[124*int(length/numero):125*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM124 = np.row_stack((globalFM124,dataArray))
		M += 1
	print(M)

	for dict in dictsList[125*int(length/numero):126*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM125 = np.row_stack((globalFM125,dataArray))
		M += 1
	print(M)

	for dict in dictsList[126*int(length/numero):127*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM126 = np.row_stack((globalFM126,dataArray))
		M += 1
	print(M)

	for dict in dictsList[127*int(length/numero):128*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM127 = np.row_stack((globalFM127,dataArray))
		M += 1
	print(M)

	for dict in dictsList[128*int(length/numero):129*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM128 = np.row_stack((globalFM128,dataArray))
		M += 1
	print(M)

	for dict in dictsList[129*int(length/numero):130*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM129 = np.row_stack((globalFM129,dataArray))
		M += 1
	print(M)

	for dict in dictsList[130*int(length/numero):131*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM130 = np.row_stack((globalFM130,dataArray))
		M += 1
	print(M)

	for dict in dictsList[131*int(length/numero):132*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM131 = np.row_stack((globalFM131,dataArray))
		M += 1
	print(M)

	for dict in dictsList[132*int(length/numero):133*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM132 = np.row_stack((globalFM132,dataArray))
		M += 1
	print(M)

	for dict in dictsList[133*int(length/numero):134*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM133 = np.row_stack((globalFM133,dataArray))
		M += 1
	print(M)

	for dict in dictsList[134*int(length/numero):135*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM134 = np.row_stack((globalFM134,dataArray))
		M += 1
	print(M)

	for dict in dictsList[135*int(length/numero):136*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM135 = np.row_stack((globalFM135,dataArray))
		M += 1
	print(M)

	for dict in dictsList[136*int(length/numero):137*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM136 = np.row_stack((globalFM136,dataArray))
		M += 1
	print(M)

	for dict in dictsList[137*int(length/numero):138*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM137 = np.row_stack((globalFM137,dataArray))
		M += 1
	print(M)

	for dict in dictsList[138*int(length/numero):139*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM138 = np.row_stack((globalFM138,dataArray))
		M += 1
	print(M)

	for dict in dictsList[139*int(length/numero):140*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM139 = np.row_stack((globalFM139,dataArray))
		M += 1
	print(M)

	for dict in dictsList[140*int(length/numero):141*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM140 = np.row_stack((globalFM140,dataArray))
		M += 1
	print(M)

	for dict in dictsList[141*int(length/numero):142*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM141 = np.row_stack((globalFM141,dataArray))
		M += 1
	print(M)

	for dict in dictsList[142*int(length/numero):143*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM142 = np.row_stack((globalFM142,dataArray))
		M += 1
	print(M)

	for dict in dictsList[143*int(length/numero):144*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM143 = np.row_stack((globalFM143,dataArray))
		M += 1
	print(M)

	for dict in dictsList[144*int(length/numero):145*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM144 = np.row_stack((globalFM144,dataArray))
		M += 1
	print(M)

	for dict in dictsList[145*int(length/numero):146*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM145 = np.row_stack((globalFM145,dataArray))
		M += 1
	print(M)

	for dict in dictsList[146*int(length/numero):147*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM146 = np.row_stack((globalFM146,dataArray))
		M += 1
	print(M)

	for dict in dictsList[147*int(length/numero):148*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM147 = np.row_stack((globalFM147,dataArray))
		M += 1
	print(M)

	for dict in dictsList[148*int(length/numero):149*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM148 = np.row_stack((globalFM148,dataArray))
		M += 1
	print(M)

	for dict in dictsList[149*int(length/numero):150*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM149 = np.row_stack((globalFM149,dataArray))
		M += 1
	print(M)

	for dict in dictsList[150*int(length/numero):151*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM150 = np.row_stack((globalFM150,dataArray))
		M += 1
	print(M)

	for dict in dictsList[151*int(length/numero):152*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM151 = np.row_stack((globalFM151,dataArray))
		M += 1
	print(M)

	for dict in dictsList[152*int(length/numero):153*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM152 = np.row_stack((globalFM152,dataArray))
		M += 1
	print(M)

	for dict in dictsList[153*int(length/numero):154*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM153 = np.row_stack((globalFM153,dataArray))
		M += 1
	print(M)

	for dict in dictsList[154*int(length/numero):155*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM154 = np.row_stack((globalFM154,dataArray))
		M += 1
	print(M)

	for dict in dictsList[155*int(length/numero):156*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM155 = np.row_stack((globalFM155,dataArray))
		M += 1
	print(M)

	for dict in dictsList[156*int(length/numero):157*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM156 = np.row_stack((globalFM156,dataArray))
		M += 1
	print(M)

	for dict in dictsList[157*int(length/numero):158*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM157 = np.row_stack((globalFM157,dataArray))
		M += 1
	print(M)

	for dict in dictsList[158*int(length/numero):159*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM158 = np.row_stack((globalFM158,dataArray))
		M += 1
	print(M)

	for dict in dictsList[159*int(length/numero):160*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM159 = np.row_stack((globalFM159,dataArray))
		M += 1
	print(M)

	for dict in dictsList[160*int(length/numero):161*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM160 = np.row_stack((globalFM160,dataArray))
		M += 1
	print(M)

	for dict in dictsList[161*int(length/numero):162*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM161 = np.row_stack((globalFM161,dataArray))
		M += 1
	print(M)

	for dict in dictsList[162*int(length/numero):163*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM162 = np.row_stack((globalFM162,dataArray))
		M += 1
	print(M)

	for dict in dictsList[163*int(length/numero):164*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM163 = np.row_stack((globalFM163,dataArray))
		M += 1
	print(M)

	for dict in dictsList[164*int(length/numero):165*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM164 = np.row_stack((globalFM164,dataArray))
		M += 1
	print(M)

	for dict in dictsList[165*int(length/numero):166*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM165 = np.row_stack((globalFM165,dataArray))
		M += 1
	print(M)

	for dict in dictsList[166*int(length/numero):167*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM166 = np.row_stack((globalFM166,dataArray))
		M += 1
	print(M)

	for dict in dictsList[167*int(length/numero):168*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM167 = np.row_stack((globalFM167,dataArray))
		M += 1
	print(M)

	for dict in dictsList[168*int(length/numero):169*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM168 = np.row_stack((globalFM168,dataArray))
		M += 1
	print(M)

	for dict in dictsList[169*int(length/numero):170*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM169 = np.row_stack((globalFM169,dataArray))
		M += 1
	print(M)

	for dict in dictsList[170*int(length/numero):171*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM170 = np.row_stack((globalFM170,dataArray))
		M += 1
	print(M)

	for dict in dictsList[171*int(length/numero):172*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM171 = np.row_stack((globalFM171,dataArray))
		M += 1
	print(M)

	for dict in dictsList[172*int(length/numero):173*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM172 = np.row_stack((globalFM172,dataArray))
		M += 1
	print(M)

	for dict in dictsList[173*int(length/numero):174*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM173 = np.row_stack((globalFM173,dataArray))
		M += 1
	print(M)

	for dict in dictsList[174*int(length/numero):175*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM174 = np.row_stack((globalFM174,dataArray))
		M += 1
	print(M)

	for dict in dictsList[175*int(length/numero):176*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM175 = np.row_stack((globalFM175,dataArray))
		M += 1
	print(M)

	for dict in dictsList[176*int(length/numero):177*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM176 = np.row_stack((globalFM176,dataArray))
		M += 1
	print(M)

	for dict in dictsList[177*int(length/numero):178*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM177 = np.row_stack((globalFM177,dataArray))
		M += 1
	print(M)

	for dict in dictsList[178*int(length/numero):179*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM178 = np.row_stack((globalFM178,dataArray))
		M += 1
	print(M)

	for dict in dictsList[179*int(length/numero):180*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM179 = np.row_stack((globalFM179,dataArray))
		M += 1
	print(M)

	for dict in dictsList[180*int(length/numero):181*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM180 = np.row_stack((globalFM180,dataArray))
		M += 1
	print(M)

	for dict in dictsList[181*int(length/numero):182*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM181 = np.row_stack((globalFM181,dataArray))
		M += 1
	print(M)

	for dict in dictsList[182*int(length/numero):183*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM182 = np.row_stack((globalFM182,dataArray))
		M += 1
	print(M)

	for dict in dictsList[183*int(length/numero):184*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM183 = np.row_stack((globalFM183,dataArray))
		M += 1
	print(M)

	for dict in dictsList[184*int(length/numero):185*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM184 = np.row_stack((globalFM184,dataArray))
		M += 1
	print(M)

	for dict in dictsList[185*int(length/numero):186*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM185 = np.row_stack((globalFM185,dataArray))
		M += 1
	print(M)

	for dict in dictsList[186*int(length/numero):187*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM186 = np.row_stack((globalFM186,dataArray))
		M += 1
	print(M)

	for dict in dictsList[187*int(length/numero):188*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM187 = np.row_stack((globalFM187,dataArray))
		M += 1
	print(M)

	for dict in dictsList[188*int(length/numero):189*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM188 = np.row_stack((globalFM188,dataArray))
		M += 1
	print(M)

	for dict in dictsList[189*int(length/numero):190*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM189 = np.row_stack((globalFM189,dataArray))
		M += 1
	print(M)

	for dict in dictsList[190*int(length/numero):191*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM190 = np.row_stack((globalFM190,dataArray))
		M += 1
	print(M)

	for dict in dictsList[191*int(length/numero):192*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM191 = np.row_stack((globalFM191,dataArray))
		M += 1
	print(M)

	for dict in dictsList[192*int(length/numero):193*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM192 = np.row_stack((globalFM192,dataArray))
		M += 1
	print(M)

	for dict in dictsList[193*int(length/numero):194*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM193 = np.row_stack((globalFM193,dataArray))
		M += 1
	print(M)

	for dict in dictsList[194*int(length/numero):195*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM194 = np.row_stack((globalFM194,dataArray))
		M += 1
	print(M)

	for dict in dictsList[195*int(length/numero):196*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM195 = np.row_stack((globalFM195,dataArray))
		M += 1
	print(M)

	for dict in dictsList[196*int(length/numero):197*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM196 = np.row_stack((globalFM196,dataArray))
		M += 1
	print(M)

	for dict in dictsList[197*int(length/numero):198*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM197 = np.row_stack((globalFM197,dataArray))
		M += 1
	print(M)

	for dict in dictsList[198*int(length/numero):199*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM198 = np.row_stack((globalFM198,dataArray))
		M += 1
	print(M)

	for dict in dictsList[199*int(length/numero):200*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM199 = np.row_stack((globalFM199,dataArray))
		M += 1
	print(M)

	for dict in dictsList[200*int(length/numero):201*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM200 = np.row_stack((globalFM200,dataArray))
		M += 1
	print(M)

	for dict in dictsList[201*int(length/numero):202*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM201 = np.row_stack((globalFM201,dataArray))
		M += 1
	print(M)

	for dict in dictsList[202*int(length/numero):203*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM202 = np.row_stack((globalFM202,dataArray))
		M += 1
	print(M)

	for dict in dictsList[203*int(length/numero):204*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM203 = np.row_stack((globalFM203,dataArray))
		M += 1
	print(M)

	for dict in dictsList[204*int(length/numero):205*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM204 = np.row_stack((globalFM204,dataArray))
		M += 1
	print(M)

	for dict in dictsList[205*int(length/numero):206*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM205 = np.row_stack((globalFM205,dataArray))
		M += 1
	print(M)

	for dict in dictsList[206*int(length/numero):207*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM206 = np.row_stack((globalFM206,dataArray))
		M += 1
	print(M)

	for dict in dictsList[207*int(length/numero):208*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM207 = np.row_stack((globalFM207,dataArray))
		M += 1
	print(M)

	for dict in dictsList[208*int(length/numero):209*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM208 = np.row_stack((globalFM208,dataArray))
		M += 1
	print(M)

	for dict in dictsList[209*int(length/numero):210*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM209 = np.row_stack((globalFM209,dataArray))
		M += 1
	print(M)

	for dict in dictsList[210*int(length/numero):211*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM210 = np.row_stack((globalFM210,dataArray))
		M += 1
	print(M)

	for dict in dictsList[211*int(length/numero):212*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM211 = np.row_stack((globalFM211,dataArray))
		M += 1
	print(M)

	for dict in dictsList[212*int(length/numero):213*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM212 = np.row_stack((globalFM212,dataArray))
		M += 1
	print(M)

	for dict in dictsList[213*int(length/numero):214*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM213 = np.row_stack((globalFM213,dataArray))
		M += 1
	print(M)

	for dict in dictsList[214*int(length/numero):215*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM214 = np.row_stack((globalFM214,dataArray))
		M += 1
	print(M)

	for dict in dictsList[215*int(length/numero):216*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM215 = np.row_stack((globalFM215,dataArray))
		M += 1
	print(M)

	for dict in dictsList[216*int(length/numero):217*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM216 = np.row_stack((globalFM216,dataArray))
		M += 1
	print(M)

	for dict in dictsList[217*int(length/numero):218*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM217 = np.row_stack((globalFM217,dataArray))
		M += 1
	print(M)

	for dict in dictsList[218*int(length/numero):219*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM218 = np.row_stack((globalFM218,dataArray))
		M += 1
	print(M)

	for dict in dictsList[219*int(length/numero):220*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM219 = np.row_stack((globalFM219,dataArray))
		M += 1
	print(M)

	for dict in dictsList[220*int(length/numero):221*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM220 = np.row_stack((globalFM220,dataArray))
		M += 1
	print(M)

	for dict in dictsList[221*int(length/numero):222*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM221 = np.row_stack((globalFM221,dataArray))
		M += 1
	print(M)

	for dict in dictsList[222*int(length/numero):223*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM222 = np.row_stack((globalFM222,dataArray))
		M += 1
	print(M)

	for dict in dictsList[223*int(length/numero):224*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM223 = np.row_stack((globalFM223,dataArray))
		M += 1
	print(M)

	for dict in dictsList[224*int(length/numero):225*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM224 = np.row_stack((globalFM224,dataArray))
		M += 1
	print(M)

	for dict in dictsList[225*int(length/numero):226*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM225 = np.row_stack((globalFM225,dataArray))
		M += 1
	print(M)

	for dict in dictsList[226*int(length/numero):227*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM226 = np.row_stack((globalFM226,dataArray))
		M += 1
	print(M)

	for dict in dictsList[227*int(length/numero):228*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM227 = np.row_stack((globalFM227,dataArray))
		M += 1
	print(M)

	for dict in dictsList[228*int(length/numero):229*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM228 = np.row_stack((globalFM228,dataArray))
		M += 1
	print(M)

	for dict in dictsList[229*int(length/numero):230*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM229 = np.row_stack((globalFM229,dataArray))
		M += 1
	print(M)

	for dict in dictsList[230*int(length/numero):231*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM230 = np.row_stack((globalFM230,dataArray))
		M += 1
	print(M)

	for dict in dictsList[231*int(length/numero):232*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM231 = np.row_stack((globalFM231,dataArray))
		M += 1
	print(M)

	for dict in dictsList[232*int(length/numero):233*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM232 = np.row_stack((globalFM232,dataArray))
		M += 1
	print(M)

	for dict in dictsList[233*int(length/numero):234*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM233 = np.row_stack((globalFM233,dataArray))
		M += 1
	print(M)

	for dict in dictsList[234*int(length/numero):235*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM234 = np.row_stack((globalFM234,dataArray))
		M += 1
	print(M)

	for dict in dictsList[235*int(length/numero):236*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM235 = np.row_stack((globalFM235,dataArray))
		M += 1
	print(M)

	for dict in dictsList[236*int(length/numero):237*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM236 = np.row_stack((globalFM236,dataArray))
		M += 1
	print(M)

	for dict in dictsList[237*int(length/numero):238*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM237 = np.row_stack((globalFM237,dataArray))
		M += 1
	print(M)

	for dict in dictsList[238*int(length/numero):239*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM238 = np.row_stack((globalFM238,dataArray))
		M += 1
	print(M)

	for dict in dictsList[239*int(length/numero):240*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM239 = np.row_stack((globalFM239,dataArray))
		M += 1
	print(M)

	for dict in dictsList[240*int(length/numero):241*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM240 = np.row_stack((globalFM240,dataArray))
		M += 1
	print(M)

	for dict in dictsList[241*int(length/numero):242*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM241 = np.row_stack((globalFM241,dataArray))
		M += 1
	print(M)

	for dict in dictsList[242*int(length/numero):243*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM242 = np.row_stack((globalFM242,dataArray))
		M += 1
	print(M)

	for dict in dictsList[243*int(length/numero):244*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM243 = np.row_stack((globalFM243,dataArray))
		M += 1
	print(M)

	for dict in dictsList[244*int(length/numero):245*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM244 = np.row_stack((globalFM244,dataArray))
		M += 1
	print(M)

	for dict in dictsList[245*int(length/numero):246*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM245 = np.row_stack((globalFM245,dataArray))
		M += 1
	print(M)

	for dict in dictsList[246*int(length/numero):247*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM246 = np.row_stack((globalFM246,dataArray))
		M += 1
	print(M)

	for dict in dictsList[247*int(length/numero):248*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM247 = np.row_stack((globalFM247,dataArray))
		M += 1
	print(M)

	for dict in dictsList[248*int(length/numero):249*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM248 = np.row_stack((globalFM248,dataArray))
		M += 1
	print(M)

	for dict in dictsList[249*int(length/numero):250*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM249 = np.row_stack((globalFM249,dataArray))
		M += 1
	print(M)

	for dict in dictsList[250*int(length/numero):251*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM250 = np.row_stack((globalFM250,dataArray))
		M += 1
	print(M)

	for dict in dictsList[251*int(length/numero):252*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM251 = np.row_stack((globalFM251,dataArray))
		M += 1
	print(M)

	for dict in dictsList[252*int(length/numero):253*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM252 = np.row_stack((globalFM252,dataArray))
		M += 1
	print(M)

	for dict in dictsList[253*int(length/numero):254*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM253 = np.row_stack((globalFM253,dataArray))
		M += 1
	print(M)

	for dict in dictsList[254*int(length/numero):255*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM254 = np.row_stack((globalFM254,dataArray))
		M += 1
	print(M)

	for dict in dictsList[255*int(length/numero):256*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM255 = np.row_stack((globalFM255,dataArray))
		M += 1
	print(M)

	for dict in dictsList[256*int(length/numero):257*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM256 = np.row_stack((globalFM256,dataArray))
		M += 1
	print(M)

	for dict in dictsList[257*int(length/numero):258*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM257 = np.row_stack((globalFM257,dataArray))
		M += 1
	print(M)

	for dict in dictsList[258*int(length/numero):259*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM258 = np.row_stack((globalFM258,dataArray))
		M += 1
	print(M)

	for dict in dictsList[259*int(length/numero):260*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM259 = np.row_stack((globalFM259,dataArray))
		M += 1
	print(M)

	for dict in dictsList[260*int(length/numero):261*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM260 = np.row_stack((globalFM260,dataArray))
		M += 1
	print(M)

	for dict in dictsList[261*int(length/numero):262*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM261 = np.row_stack((globalFM261,dataArray))
		M += 1
	print(M)

	for dict in dictsList[262*int(length/numero):263*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM262 = np.row_stack((globalFM262,dataArray))
		M += 1
	print(M)

	for dict in dictsList[263*int(length/numero):264*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM263 = np.row_stack((globalFM263,dataArray))
		M += 1
	print(M)

	for dict in dictsList[264*int(length/numero):265*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM264 = np.row_stack((globalFM264,dataArray))
		M += 1
	print(M)

	for dict in dictsList[265*int(length/numero):266*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM265 = np.row_stack((globalFM265,dataArray))
		M += 1
	print(M)

	for dict in dictsList[266*int(length/numero):267*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM266 = np.row_stack((globalFM266,dataArray))
		M += 1
	print(M)

	for dict in dictsList[267*int(length/numero):268*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM267 = np.row_stack((globalFM267,dataArray))
		M += 1
	print(M)

	for dict in dictsList[268*int(length/numero):269*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM268 = np.row_stack((globalFM268,dataArray))
		M += 1
	print(M)

	for dict in dictsList[269*int(length/numero):270*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM269 = np.row_stack((globalFM269,dataArray))
		M += 1
	print(M)

	for dict in dictsList[270*int(length/numero):271*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM270 = np.row_stack((globalFM270,dataArray))
		M += 1
	print(M)

	for dict in dictsList[271*int(length/numero):272*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM271 = np.row_stack((globalFM271,dataArray))
		M += 1
	print(M)

	for dict in dictsList[272*int(length/numero):273*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM272 = np.row_stack((globalFM272,dataArray))
		M += 1
	print(M)

	for dict in dictsList[273*int(length/numero):274*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM273 = np.row_stack((globalFM273,dataArray))
		M += 1
	print(M)

	for dict in dictsList[274*int(length/numero):275*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM274 = np.row_stack((globalFM274,dataArray))
		M += 1
	print(M)

	for dict in dictsList[275*int(length/numero):276*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM275 = np.row_stack((globalFM275,dataArray))
		M += 1
	print(M)

	for dict in dictsList[276*int(length/numero):277*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM276 = np.row_stack((globalFM276,dataArray))
		M += 1
	print(M)

	for dict in dictsList[277*int(length/numero):278*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM277 = np.row_stack((globalFM277,dataArray))
		M += 1
	print(M)

	for dict in dictsList[278*int(length/numero):279*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM278 = np.row_stack((globalFM278,dataArray))
		M += 1
	print(M)

	for dict in dictsList[279*int(length/numero):280*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM279 = np.row_stack((globalFM279,dataArray))
		M += 1
	print(M)

	for dict in dictsList[280*int(length/numero):281*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM280 = np.row_stack((globalFM280,dataArray))
		M += 1
	print(M)

	for dict in dictsList[281*int(length/numero):282*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM281 = np.row_stack((globalFM281,dataArray))
		M += 1
	print(M)

	for dict in dictsList[282*int(length/numero):283*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM282 = np.row_stack((globalFM282,dataArray))
		M += 1
	print(M)

	for dict in dictsList[283*int(length/numero):284*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM283 = np.row_stack((globalFM283,dataArray))
		M += 1
	print(M)

	for dict in dictsList[284*int(length/numero):285*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM284 = np.row_stack((globalFM284,dataArray))
		M += 1
	print(M)

	for dict in dictsList[285*int(length/numero):286*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM285 = np.row_stack((globalFM285,dataArray))
		M += 1
	print(M)

	for dict in dictsList[286*int(length/numero):287*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM286 = np.row_stack((globalFM286,dataArray))
		M += 1
	print(M)

	for dict in dictsList[287*int(length/numero):288*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM287 = np.row_stack((globalFM287,dataArray))
		M += 1
	print(M)

	for dict in dictsList[288*int(length/numero):289*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM288 = np.row_stack((globalFM288,dataArray))
		M += 1
	print(M)

	for dict in dictsList[289*int(length/numero):290*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM289 = np.row_stack((globalFM289,dataArray))
		M += 1
	print(M)

	for dict in dictsList[290*int(length/numero):291*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM290 = np.row_stack((globalFM290,dataArray))
		M += 1
	print(M)

	for dict in dictsList[291*int(length/numero):292*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM291 = np.row_stack((globalFM291,dataArray))
		M += 1
	print(M)

	for dict in dictsList[292*int(length/numero):293*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM292 = np.row_stack((globalFM292,dataArray))
		M += 1
	print(M)

	for dict in dictsList[293*int(length/numero):294*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM293 = np.row_stack((globalFM293,dataArray))
		M += 1
	print(M)

	for dict in dictsList[294*int(length/numero):295*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM294 = np.row_stack((globalFM294,dataArray))
		M += 1
	print(M)

	for dict in dictsList[295*int(length/numero):296*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM295 = np.row_stack((globalFM295,dataArray))
		M += 1
	print(M)

	for dict in dictsList[296*int(length/numero):297*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM296 = np.row_stack((globalFM296,dataArray))
		M += 1
	print(M)

	for dict in dictsList[297*int(length/numero):298*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM297 = np.row_stack((globalFM297,dataArray))
		M += 1
	print(M)

	for dict in dictsList[298*int(length/numero):299*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM298 = np.row_stack((globalFM298,dataArray))
		M += 1
	print(M)

	for dict in dictsList[299*int(length/numero):300*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM299 = np.row_stack((globalFM299,dataArray))
		M += 1
	print(M)

	for dict in dictsList[300*int(length/numero):301*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM300 = np.row_stack((globalFM300,dataArray))
		M += 1
	print(M)

	for dict in dictsList[301*int(length/numero):302*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM301 = np.row_stack((globalFM301,dataArray))
		M += 1
	print(M)

	for dict in dictsList[302*int(length/numero):303*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM302 = np.row_stack((globalFM302,dataArray))
		M += 1
	print(M)

	for dict in dictsList[303*int(length/numero):304*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM303 = np.row_stack((globalFM303,dataArray))
		M += 1
	print(M)

	for dict in dictsList[304*int(length/numero):305*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM304 = np.row_stack((globalFM304,dataArray))
		M += 1
	print(M)

	for dict in dictsList[305*int(length/numero):306*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM305 = np.row_stack((globalFM305,dataArray))
		M += 1
	print(M)

	for dict in dictsList[306*int(length/numero):307*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM306 = np.row_stack((globalFM306,dataArray))
		M += 1
	print(M)

	for dict in dictsList[307*int(length/numero):308*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM307 = np.row_stack((globalFM307,dataArray))
		M += 1
	print(M)

	for dict in dictsList[308*int(length/numero):309*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM308 = np.row_stack((globalFM308,dataArray))
		M += 1
	print(M)

	for dict in dictsList[309*int(length/numero):310*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM309 = np.row_stack((globalFM309,dataArray))
		M += 1
	print(M)

	for dict in dictsList[310*int(length/numero):311*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM310 = np.row_stack((globalFM310,dataArray))
		M += 1
	print(M)

	for dict in dictsList[311*int(length/numero):312*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM311 = np.row_stack((globalFM311,dataArray))
		M += 1
	print(M)

	for dict in dictsList[312*int(length/numero):313*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM312 = np.row_stack((globalFM312,dataArray))
		M += 1
	print(M)

	for dict in dictsList[313*int(length/numero):314*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM313 = np.row_stack((globalFM313,dataArray))
		M += 1
	print(M)

	for dict in dictsList[314*int(length/numero):315*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM314 = np.row_stack((globalFM314,dataArray))
		M += 1
	print(M)

	for dict in dictsList[315*int(length/numero):316*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM315 = np.row_stack((globalFM315,dataArray))
		M += 1
	print(M)

	for dict in dictsList[316*int(length/numero):317*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM316 = np.row_stack((globalFM316,dataArray))
		M += 1
	print(M)

	for dict in dictsList[317*int(length/numero):318*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM317 = np.row_stack((globalFM317,dataArray))
		M += 1
	print(M)

	for dict in dictsList[318*int(length/numero):319*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM318 = np.row_stack((globalFM318,dataArray))
		M += 1
	print(M)

	for dict in dictsList[319*int(length/numero):320*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM319 = np.row_stack((globalFM319,dataArray))
		M += 1
	print(M)

	for dict in dictsList[320*int(length/numero):321*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM320 = np.row_stack((globalFM320,dataArray))
		M += 1
	print(M)

	for dict in dictsList[321*int(length/numero):322*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM321 = np.row_stack((globalFM321,dataArray))
		M += 1
	print(M)

	for dict in dictsList[322*int(length/numero):323*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM322 = np.row_stack((globalFM322,dataArray))
		M += 1
	print(M)

	for dict in dictsList[323*int(length/numero):324*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM323 = np.row_stack((globalFM323,dataArray))
		M += 1
	print(M)

	for dict in dictsList[324*int(length/numero):325*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM324 = np.row_stack((globalFM324,dataArray))
		M += 1
	print(M)

	for dict in dictsList[325*int(length/numero):326*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM325 = np.row_stack((globalFM325,dataArray))
		M += 1
	print(M)

	for dict in dictsList[326*int(length/numero):327*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM326 = np.row_stack((globalFM326,dataArray))
		M += 1
	print(M)

	for dict in dictsList[327*int(length/numero):328*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM327 = np.row_stack((globalFM327,dataArray))
		M += 1
	print(M)

	for dict in dictsList[328*int(length/numero):329*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM328 = np.row_stack((globalFM328,dataArray))
		M += 1
	print(M)

	for dict in dictsList[329*int(length/numero):330*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM329 = np.row_stack((globalFM329,dataArray))
		M += 1
	print(M)

	for dict in dictsList[330*int(length/numero):331*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM330 = np.row_stack((globalFM330,dataArray))
		M += 1
	print(M)

	for dict in dictsList[331*int(length/numero):332*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM331 = np.row_stack((globalFM331,dataArray))
		M += 1
	print(M)

	for dict in dictsList[332*int(length/numero):333*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM332 = np.row_stack((globalFM332,dataArray))
		M += 1
	print(M)

	for dict in dictsList[333*int(length/numero):334*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM333 = np.row_stack((globalFM333,dataArray))
		M += 1
	print(M)

	for dict in dictsList[334*int(length/numero):335*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM334 = np.row_stack((globalFM334,dataArray))
		M += 1
	print(M)

	for dict in dictsList[335*int(length/numero):336*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM335 = np.row_stack((globalFM335,dataArray))
		M += 1
	print(M)

	for dict in dictsList[336*int(length/numero):337*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM336 = np.row_stack((globalFM336,dataArray))
		M += 1
	print(M)

	for dict in dictsList[337*int(length/numero):338*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM337 = np.row_stack((globalFM337,dataArray))
		M += 1
	print(M)

	for dict in dictsList[338*int(length/numero):339*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM338 = np.row_stack((globalFM338,dataArray))
		M += 1
	print(M)

	for dict in dictsList[339*int(length/numero):340*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM339 = np.row_stack((globalFM339,dataArray))
		M += 1
	print(M)

	for dict in dictsList[340*int(length/numero):341*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM340 = np.row_stack((globalFM340,dataArray))
		M += 1
	print(M)

	for dict in dictsList[341*int(length/numero):342*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM341 = np.row_stack((globalFM341,dataArray))
		M += 1
	print(M)

	for dict in dictsList[342*int(length/numero):343*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM342 = np.row_stack((globalFM342,dataArray))
		M += 1
	print(M)

	for dict in dictsList[343*int(length/numero):344*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM343 = np.row_stack((globalFM343,dataArray))
		M += 1
	print(M)

	for dict in dictsList[344*int(length/numero):345*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM344 = np.row_stack((globalFM344,dataArray))
		M += 1
	print(M)

	for dict in dictsList[345*int(length/numero):346*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM345 = np.row_stack((globalFM345,dataArray))
		M += 1
	print(M)

	for dict in dictsList[346*int(length/numero):347*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM346 = np.row_stack((globalFM346,dataArray))
		M += 1
	print(M)

	for dict in dictsList[347*int(length/numero):348*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM347 = np.row_stack((globalFM347,dataArray))
		M += 1
	print(M)

	for dict in dictsList[348*int(length/numero):349*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM348 = np.row_stack((globalFM348,dataArray))
		M += 1
	print(M)

	for dict in dictsList[349*int(length/numero):350*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM349 = np.row_stack((globalFM349,dataArray))
		M += 1
	print(M)

	for dict in dictsList[350*int(length/numero):351*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM350 = np.row_stack((globalFM350,dataArray))
		M += 1
	print(M)

	for dict in dictsList[351*int(length/numero):352*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM351 = np.row_stack((globalFM351,dataArray))
		M += 1
	print(M)

	for dict in dictsList[352*int(length/numero):353*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM352 = np.row_stack((globalFM352,dataArray))
		M += 1
	print(M)

	for dict in dictsList[353*int(length/numero):354*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM353 = np.row_stack((globalFM353,dataArray))
		M += 1
	print(M)

	for dict in dictsList[354*int(length/numero):355*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM354 = np.row_stack((globalFM354,dataArray))
		M += 1
	print(M)

	for dict in dictsList[355*int(length/numero):356*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM355 = np.row_stack((globalFM355,dataArray))
		M += 1
	print(M)

	for dict in dictsList[356*int(length/numero):357*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM356 = np.row_stack((globalFM356,dataArray))
		M += 1
	print(M)

	for dict in dictsList[357*int(length/numero):358*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM357 = np.row_stack((globalFM357,dataArray))
		M += 1
	print(M)

	for dict in dictsList[358*int(length/numero):359*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM358 = np.row_stack((globalFM358,dataArray))
		M += 1
	print(M)

	for dict in dictsList[359*int(length/numero):360*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM359 = np.row_stack((globalFM359,dataArray))
		M += 1
	print(M)

	for dict in dictsList[360*int(length/numero):361*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM360 = np.row_stack((globalFM360,dataArray))
		M += 1
	print(M)

	for dict in dictsList[361*int(length/numero):362*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM361 = np.row_stack((globalFM361,dataArray))
		M += 1
	print(M)

	for dict in dictsList[362*int(length/numero):363*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM362 = np.row_stack((globalFM362,dataArray))
		M += 1
	print(M)

	for dict in dictsList[363*int(length/numero):364*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM363 = np.row_stack((globalFM363,dataArray))
		M += 1
	print(M)

	for dict in dictsList[364*int(length/numero):365*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM364 = np.row_stack((globalFM364,dataArray))
		M += 1
	print(M)

	for dict in dictsList[365*int(length/numero):366*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM365 = np.row_stack((globalFM365,dataArray))
		M += 1
	print(M)

	for dict in dictsList[366*int(length/numero):367*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM366 = np.row_stack((globalFM366,dataArray))
		M += 1
	print(M)

	for dict in dictsList[367*int(length/numero):368*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM367 = np.row_stack((globalFM367,dataArray))
		M += 1
	print(M)

	for dict in dictsList[368*int(length/numero):369*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM368 = np.row_stack((globalFM368,dataArray))
		M += 1
	print(M)

	for dict in dictsList[369*int(length/numero):370*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM369 = np.row_stack((globalFM369,dataArray))
		M += 1
	print(M)

	for dict in dictsList[370*int(length/numero):371*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM370 = np.row_stack((globalFM370,dataArray))
		M += 1
	print(M)

	for dict in dictsList[371*int(length/numero):372*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM371 = np.row_stack((globalFM371,dataArray))
		M += 1
	print(M)

	for dict in dictsList[372*int(length/numero):373*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM372 = np.row_stack((globalFM372,dataArray))
		M += 1
	print(M)

	for dict in dictsList[373*int(length/numero):374*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM373 = np.row_stack((globalFM373,dataArray))
		M += 1
	print(M)

	for dict in dictsList[374*int(length/numero):375*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM374 = np.row_stack((globalFM374,dataArray))
		M += 1
	print(M)

	for dict in dictsList[375*int(length/numero):376*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM375 = np.row_stack((globalFM375,dataArray))
		M += 1
	print(M)

	for dict in dictsList[376*int(length/numero):377*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM376 = np.row_stack((globalFM376,dataArray))
		M += 1
	print(M)

	for dict in dictsList[377*int(length/numero):378*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM377 = np.row_stack((globalFM377,dataArray))
		M += 1
	print(M)

	for dict in dictsList[378*int(length/numero):379*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM378 = np.row_stack((globalFM378,dataArray))
		M += 1
	print(M)

	for dict in dictsList[379*int(length/numero):380*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM379 = np.row_stack((globalFM379,dataArray))
		M += 1
	print(M)

	for dict in dictsList[380*int(length/numero):381*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM380 = np.row_stack((globalFM380,dataArray))
		M += 1
	print(M)

	for dict in dictsList[381*int(length/numero):382*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM381 = np.row_stack((globalFM381,dataArray))
		M += 1
	print(M)

	for dict in dictsList[382*int(length/numero):383*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM382 = np.row_stack((globalFM382,dataArray))
		M += 1
	print(M)

	for dict in dictsList[383*int(length/numero):384*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM383 = np.row_stack((globalFM383,dataArray))
		M += 1
	print(M)

	for dict in dictsList[384*int(length/numero):385*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM384 = np.row_stack((globalFM384,dataArray))
		M += 1
	print(M)

	for dict in dictsList[385*int(length/numero):386*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM385 = np.row_stack((globalFM385,dataArray))
		M += 1
	print(M)

	for dict in dictsList[386*int(length/numero):387*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM386 = np.row_stack((globalFM386,dataArray))
		M += 1
	print(M)

	for dict in dictsList[387*int(length/numero):388*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM387 = np.row_stack((globalFM387,dataArray))
		M += 1
	print(M)

	for dict in dictsList[388*int(length/numero):389*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM388 = np.row_stack((globalFM388,dataArray))
		M += 1
	print(M)

	for dict in dictsList[389*int(length/numero):390*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM389 = np.row_stack((globalFM389,dataArray))
		M += 1
	print(M)

	for dict in dictsList[390*int(length/numero):391*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM390 = np.row_stack((globalFM390,dataArray))
		M += 1
	print(M)

	for dict in dictsList[391*int(length/numero):392*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM391 = np.row_stack((globalFM391,dataArray))
		M += 1
	print(M)

	for dict in dictsList[392*int(length/numero):393*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM392 = np.row_stack((globalFM392,dataArray))
		M += 1
	print(M)

	for dict in dictsList[393*int(length/numero):394*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM393 = np.row_stack((globalFM393,dataArray))
		M += 1
	print(M)

	for dict in dictsList[394*int(length/numero):395*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM394 = np.row_stack((globalFM394,dataArray))
		M += 1
	print(M)

	for dict in dictsList[395*int(length/numero):396*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM395 = np.row_stack((globalFM395,dataArray))
		M += 1
	print(M)

	for dict in dictsList[396*int(length/numero):397*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM396 = np.row_stack((globalFM396,dataArray))
		M += 1
	print(M)

	for dict in dictsList[397*int(length/numero):398*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM397 = np.row_stack((globalFM397,dataArray))
		M += 1
	print(M)

	for dict in dictsList[398*int(length/numero):399*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM398 = np.row_stack((globalFM398,dataArray))
		M += 1
	print(M)

	for dict in dictsList[399*int(length/numero):400*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM399 = np.row_stack((globalFM399,dataArray))
		M += 1
	print(M)

	for dict in dictsList[400*int(length/numero):401*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM400 = np.row_stack((globalFM400,dataArray))
		M += 1
	print(M)

	for dict in dictsList[401*int(length/numero):402*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM401 = np.row_stack((globalFM401,dataArray))
		M += 1
	print(M)

	for dict in dictsList[402*int(length/numero):403*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM402 = np.row_stack((globalFM402,dataArray))
		M += 1
	print(M)

	for dict in dictsList[403*int(length/numero):404*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM403 = np.row_stack((globalFM403,dataArray))
		M += 1
	print(M)

	for dict in dictsList[404*int(length/numero):405*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM404 = np.row_stack((globalFM404,dataArray))
		M += 1
	print(M)

	for dict in dictsList[405*int(length/numero):406*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM405 = np.row_stack((globalFM405,dataArray))
		M += 1
	print(M)

	for dict in dictsList[406*int(length/numero):407*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM406 = np.row_stack((globalFM406,dataArray))
		M += 1
	print(M)

	for dict in dictsList[407*int(length/numero):408*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM407 = np.row_stack((globalFM407,dataArray))
		M += 1
	print(M)

	for dict in dictsList[408*int(length/numero):409*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM408 = np.row_stack((globalFM408,dataArray))
		M += 1
	print(M)

	for dict in dictsList[409*int(length/numero):410*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM409 = np.row_stack((globalFM409,dataArray))
		M += 1
	print(M)

	for dict in dictsList[410*int(length/numero):411*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM410 = np.row_stack((globalFM410,dataArray))
		M += 1
	print(M)

	for dict in dictsList[411*int(length/numero):412*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM411 = np.row_stack((globalFM411,dataArray))
		M += 1
	print(M)

	for dict in dictsList[412*int(length/numero):413*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM412 = np.row_stack((globalFM412,dataArray))
		M += 1
	print(M)

	for dict in dictsList[413*int(length/numero):414*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM413 = np.row_stack((globalFM413,dataArray))
		M += 1
	print(M)

	for dict in dictsList[414*int(length/numero):415*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM414 = np.row_stack((globalFM414,dataArray))
		M += 1
	print(M)

	for dict in dictsList[415*int(length/numero):416*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM415 = np.row_stack((globalFM415,dataArray))
		M += 1
	print(M)

	for dict in dictsList[416*int(length/numero):417*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM416 = np.row_stack((globalFM416,dataArray))
		M += 1
	print(M)

	for dict in dictsList[417*int(length/numero):418*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM417 = np.row_stack((globalFM417,dataArray))
		M += 1
	print(M)

	for dict in dictsList[418*int(length/numero):419*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM418 = np.row_stack((globalFM418,dataArray))
		M += 1
	print(M)

	for dict in dictsList[419*int(length/numero):420*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM419 = np.row_stack((globalFM419,dataArray))
		M += 1
	print(M)

	for dict in dictsList[420*int(length/numero):421*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM420 = np.row_stack((globalFM420,dataArray))
		M += 1
	print(M)

	for dict in dictsList[421*int(length/numero):422*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM421 = np.row_stack((globalFM421,dataArray))
		M += 1
	print(M)

	for dict in dictsList[422*int(length/numero):423*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM422 = np.row_stack((globalFM422,dataArray))
		M += 1
	print(M)

	for dict in dictsList[423*int(length/numero):424*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM423 = np.row_stack((globalFM423,dataArray))
		M += 1
	print(M)

	for dict in dictsList[424*int(length/numero):425*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM424 = np.row_stack((globalFM424,dataArray))
		M += 1
	print(M)

	for dict in dictsList[425*int(length/numero):426*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM425 = np.row_stack((globalFM425,dataArray))
		M += 1
	print(M)

	for dict in dictsList[426*int(length/numero):427*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM426 = np.row_stack((globalFM426,dataArray))
		M += 1
	print(M)

	for dict in dictsList[427*int(length/numero):428*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM427 = np.row_stack((globalFM427,dataArray))
		M += 1
	print(M)

	for dict in dictsList[428*int(length/numero):429*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM428 = np.row_stack((globalFM428,dataArray))
		M += 1
	print(M)

	for dict in dictsList[429*int(length/numero):430*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM429 = np.row_stack((globalFM429,dataArray))
		M += 1
	print(M)

	for dict in dictsList[430*int(length/numero):431*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM430 = np.row_stack((globalFM430,dataArray))
		M += 1
	print(M)

	for dict in dictsList[431*int(length/numero):432*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM431 = np.row_stack((globalFM431,dataArray))
		M += 1
	print(M)

	for dict in dictsList[432*int(length/numero):433*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM432 = np.row_stack((globalFM432,dataArray))
		M += 1
	print(M)

	for dict in dictsList[433*int(length/numero):434*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM433 = np.row_stack((globalFM433,dataArray))
		M += 1
	print(M)

	for dict in dictsList[434*int(length/numero):435*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM434 = np.row_stack((globalFM434,dataArray))
		M += 1
	print(M)

	for dict in dictsList[435*int(length/numero):436*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM435 = np.row_stack((globalFM435,dataArray))
		M += 1
	print(M)

	for dict in dictsList[436*int(length/numero):437*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM436 = np.row_stack((globalFM436,dataArray))
		M += 1
	print(M)

	for dict in dictsList[437*int(length/numero):438*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM437 = np.row_stack((globalFM437,dataArray))
		M += 1
	print(M)

	for dict in dictsList[438*int(length/numero):439*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM438 = np.row_stack((globalFM438,dataArray))
		M += 1
	print(M)

	for dict in dictsList[439*int(length/numero):440*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM439 = np.row_stack((globalFM439,dataArray))
		M += 1
	print(M)

	for dict in dictsList[440*int(length/numero):441*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM440 = np.row_stack((globalFM440,dataArray))
		M += 1
	print(M)

	for dict in dictsList[441*int(length/numero):442*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM441 = np.row_stack((globalFM441,dataArray))
		M += 1
	print(M)

	for dict in dictsList[442*int(length/numero):443*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM442 = np.row_stack((globalFM442,dataArray))
		M += 1
	print(M)

	for dict in dictsList[443*int(length/numero):444*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM443 = np.row_stack((globalFM443,dataArray))
		M += 1
	print(M)

	for dict in dictsList[444*int(length/numero):445*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM444 = np.row_stack((globalFM444,dataArray))
		M += 1
	print(M)

	for dict in dictsList[445*int(length/numero):446*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM445 = np.row_stack((globalFM445,dataArray))
		M += 1
	print(M)

	for dict in dictsList[446*int(length/numero):447*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM446 = np.row_stack((globalFM446,dataArray))
		M += 1
	print(M)

	for dict in dictsList[447*int(length/numero):448*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM447 = np.row_stack((globalFM447,dataArray))
		M += 1
	print(M)

	for dict in dictsList[448*int(length/numero):449*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM448 = np.row_stack((globalFM448,dataArray))
		M += 1
	print(M)

	for dict in dictsList[449*int(length/numero):450*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM449 = np.row_stack((globalFM449,dataArray))
		M += 1
	print(M)

	for dict in dictsList[450*int(length/numero):451*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM450 = np.row_stack((globalFM450,dataArray))
		M += 1
	print(M)

	for dict in dictsList[451*int(length/numero):452*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM451 = np.row_stack((globalFM451,dataArray))
		M += 1
	print(M)

	for dict in dictsList[452*int(length/numero):453*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM452 = np.row_stack((globalFM452,dataArray))
		M += 1
	print(M)

	for dict in dictsList[453*int(length/numero):454*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM453 = np.row_stack((globalFM453,dataArray))
		M += 1
	print(M)

	for dict in dictsList[454*int(length/numero):455*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM454 = np.row_stack((globalFM454,dataArray))
		M += 1
	print(M)

	for dict in dictsList[455*int(length/numero):456*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM455 = np.row_stack((globalFM455,dataArray))
		M += 1
	print(M)

	for dict in dictsList[456*int(length/numero):457*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM456 = np.row_stack((globalFM456,dataArray))
		M += 1
	print(M)

	for dict in dictsList[457*int(length/numero):458*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM457 = np.row_stack((globalFM457,dataArray))
		M += 1
	print(M)

	for dict in dictsList[458*int(length/numero):459*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM458 = np.row_stack((globalFM458,dataArray))
		M += 1
	print(M)

	for dict in dictsList[459*int(length/numero):460*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM459 = np.row_stack((globalFM459,dataArray))
		M += 1
	print(M)

	for dict in dictsList[460*int(length/numero):461*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM460 = np.row_stack((globalFM460,dataArray))
		M += 1
	print(M)

	for dict in dictsList[461*int(length/numero):462*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM461 = np.row_stack((globalFM461,dataArray))
		M += 1
	print(M)

	for dict in dictsList[462*int(length/numero):463*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM462 = np.row_stack((globalFM462,dataArray))
		M += 1
	print(M)

	for dict in dictsList[463*int(length/numero):464*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM463 = np.row_stack((globalFM463,dataArray))
		M += 1
	print(M)

	for dict in dictsList[464*int(length/numero):465*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM464 = np.row_stack((globalFM464,dataArray))
		M += 1
	print(M)

	for dict in dictsList[465*int(length/numero):466*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM465 = np.row_stack((globalFM465,dataArray))
		M += 1
	print(M)

	for dict in dictsList[466*int(length/numero):467*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM466 = np.row_stack((globalFM466,dataArray))
		M += 1
	print(M)

	for dict in dictsList[467*int(length/numero):468*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM467 = np.row_stack((globalFM467,dataArray))
		M += 1
	print(M)

	for dict in dictsList[468*int(length/numero):469*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM468 = np.row_stack((globalFM468,dataArray))
		M += 1
	print(M)

	for dict in dictsList[469*int(length/numero):470*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM469 = np.row_stack((globalFM469,dataArray))
		M += 1
	print(M)

	for dict in dictsList[470*int(length/numero):471*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM470 = np.row_stack((globalFM470,dataArray))
		M += 1
	print(M)

	for dict in dictsList[471*int(length/numero):472*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM471 = np.row_stack((globalFM471,dataArray))
		M += 1
	print(M)

	for dict in dictsList[472*int(length/numero):473*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM472 = np.row_stack((globalFM472,dataArray))
		M += 1
	print(M)

	for dict in dictsList[473*int(length/numero):474*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM473 = np.row_stack((globalFM473,dataArray))
		M += 1
	print(M)

	for dict in dictsList[474*int(length/numero):475*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM474 = np.row_stack((globalFM474,dataArray))
		M += 1
	print(M)

	for dict in dictsList[475*int(length/numero):476*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM475 = np.row_stack((globalFM475,dataArray))
		M += 1
	print(M)

	for dict in dictsList[476*int(length/numero):477*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM476 = np.row_stack((globalFM476,dataArray))
		M += 1
	print(M)

	for dict in dictsList[477*int(length/numero):478*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM477 = np.row_stack((globalFM477,dataArray))
		M += 1
	print(M)

	for dict in dictsList[478*int(length/numero):479*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM478 = np.row_stack((globalFM478,dataArray))
		M += 1
	print(M)

	for dict in dictsList[479*int(length/numero):480*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM479 = np.row_stack((globalFM479,dataArray))
		M += 1
	print(M)

	for dict in dictsList[480*int(length/numero):481*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM480 = np.row_stack((globalFM480,dataArray))
		M += 1
	print(M)

	for dict in dictsList[481*int(length/numero):482*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM481 = np.row_stack((globalFM481,dataArray))
		M += 1
	print(M)

	for dict in dictsList[482*int(length/numero):483*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM482 = np.row_stack((globalFM482,dataArray))
		M += 1
	print(M)

	for dict in dictsList[483*int(length/numero):484*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM483 = np.row_stack((globalFM483,dataArray))
		M += 1
	print(M)

	for dict in dictsList[484*int(length/numero):485*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM484 = np.row_stack((globalFM484,dataArray))
		M += 1
	print(M)

	for dict in dictsList[485*int(length/numero):486*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM485 = np.row_stack((globalFM485,dataArray))
		M += 1
	print(M)

	for dict in dictsList[486*int(length/numero):487*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM486 = np.row_stack((globalFM486,dataArray))
		M += 1
	print(M)

	for dict in dictsList[487*int(length/numero):488*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM487 = np.row_stack((globalFM487,dataArray))
		M += 1
	print(M)

	for dict in dictsList[488*int(length/numero):489*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM488 = np.row_stack((globalFM488,dataArray))
		M += 1
	print(M)

	for dict in dictsList[489*int(length/numero):490*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM489 = np.row_stack((globalFM489,dataArray))
		M += 1
	print(M)

	for dict in dictsList[490*int(length/numero):491*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM490 = np.row_stack((globalFM490,dataArray))
		M += 1
	print(M)

	for dict in dictsList[491*int(length/numero):492*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM491 = np.row_stack((globalFM491,dataArray))
		M += 1
	print(M)

	for dict in dictsList[492*int(length/numero):493*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM492 = np.row_stack((globalFM492,dataArray))
		M += 1
	print(M)

	for dict in dictsList[493*int(length/numero):494*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM493 = np.row_stack((globalFM493,dataArray))
		M += 1
	print(M)

	for dict in dictsList[494*int(length/numero):495*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM494 = np.row_stack((globalFM494,dataArray))
		M += 1
	print(M)

	for dict in dictsList[495*int(length/numero):496*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM495 = np.row_stack((globalFM495,dataArray))
		M += 1
	print(M)

	for dict in dictsList[496*int(length/numero):497*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM496 = np.row_stack((globalFM496,dataArray))
		M += 1
	print(M)

	for dict in dictsList[497*int(length/numero):498*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM497 = np.row_stack((globalFM497,dataArray))
		M += 1
	print(M)

	for dict in dictsList[498*int(length/numero):499*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM498 = np.row_stack((globalFM498,dataArray))
		M += 1
	print(M)

	for dict in dictsList[499*int(length/numero):500*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM499 = np.row_stack((globalFM499,dataArray))
		M += 1
	print(M)

	for dict in dictsList[500*int(length/numero):501*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM500 = np.row_stack((globalFM500,dataArray))
		M += 1
	print(M)

	for dict in dictsList[501*int(length/numero):502*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM501 = np.row_stack((globalFM501,dataArray))
		M += 1
	print(M)

	for dict in dictsList[502*int(length/numero):503*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM502 = np.row_stack((globalFM502,dataArray))
		M += 1
	print(M)

	for dict in dictsList[503*int(length/numero):504*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM503 = np.row_stack((globalFM503,dataArray))
		M += 1
	print(M)

	for dict in dictsList[504*int(length/numero):505*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM504 = np.row_stack((globalFM504,dataArray))
		M += 1
	print(M)

	for dict in dictsList[505*int(length/numero):506*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM505 = np.row_stack((globalFM505,dataArray))
		M += 1
	print(M)

	for dict in dictsList[506*int(length/numero):507*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM506 = np.row_stack((globalFM506,dataArray))
		M += 1
	print(M)

	for dict in dictsList[507*int(length/numero):508*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM507 = np.row_stack((globalFM507,dataArray))
		M += 1
	print(M)

	for dict in dictsList[508*int(length/numero):509*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM508 = np.row_stack((globalFM508,dataArray))
		M += 1
	print(M)

	for dict in dictsList[509*int(length/numero):510*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM509 = np.row_stack((globalFM509,dataArray))
		M += 1
	print(M)

	for dict in dictsList[510*int(length/numero):511*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM510 = np.row_stack((globalFM510,dataArray))
		M += 1
	print(M)

	for dict in dictsList[511*int(length/numero):512*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM511 = np.row_stack((globalFM511,dataArray))
		M += 1
	print(M)

	for dict in dictsList[512*int(length/numero):513*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM512 = np.row_stack((globalFM512,dataArray))
		M += 1
	print(M)

	for dict in dictsList[513*int(length/numero):514*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM513 = np.row_stack((globalFM513,dataArray))
		M += 1
	print(M)

	for dict in dictsList[514*int(length/numero):515*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM514 = np.row_stack((globalFM514,dataArray))
		M += 1
	print(M)

	for dict in dictsList[515*int(length/numero):516*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM515 = np.row_stack((globalFM515,dataArray))
		M += 1
	print(M)

	for dict in dictsList[516*int(length/numero):517*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM516 = np.row_stack((globalFM516,dataArray))
		M += 1
	print(M)

	for dict in dictsList[517*int(length/numero):518*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM517 = np.row_stack((globalFM517,dataArray))
		M += 1
	print(M)

	for dict in dictsList[518*int(length/numero):519*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM518 = np.row_stack((globalFM518,dataArray))
		M += 1
	print(M)

	for dict in dictsList[519*int(length/numero):520*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM519 = np.row_stack((globalFM519,dataArray))
		M += 1
	print(M)

	for dict in dictsList[520*int(length/numero):521*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM520 = np.row_stack((globalFM520,dataArray))
		M += 1
	print(M)

	for dict in dictsList[521*int(length/numero):522*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM521 = np.row_stack((globalFM521,dataArray))
		M += 1
	print(M)

	for dict in dictsList[522*int(length/numero):523*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM522 = np.row_stack((globalFM522,dataArray))
		M += 1
	print(M)

	for dict in dictsList[523*int(length/numero):524*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM523 = np.row_stack((globalFM523,dataArray))
		M += 1
	print(M)

	for dict in dictsList[524*int(length/numero):525*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM524 = np.row_stack((globalFM524,dataArray))
		M += 1
	print(M)

	for dict in dictsList[525*int(length/numero):526*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM525 = np.row_stack((globalFM525,dataArray))
		M += 1
	print(M)

	for dict in dictsList[526*int(length/numero):527*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM526 = np.row_stack((globalFM526,dataArray))
		M += 1
	print(M)

	for dict in dictsList[527*int(length/numero):528*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM527 = np.row_stack((globalFM527,dataArray))
		M += 1
	print(M)

	for dict in dictsList[528*int(length/numero):529*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM528 = np.row_stack((globalFM528,dataArray))
		M += 1
	print(M)

	for dict in dictsList[529*int(length/numero):530*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM529 = np.row_stack((globalFM529,dataArray))
		M += 1
	print(M)

	for dict in dictsList[530*int(length/numero):531*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM530 = np.row_stack((globalFM530,dataArray))
		M += 1
	print(M)

	for dict in dictsList[531*int(length/numero):532*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM531 = np.row_stack((globalFM531,dataArray))
		M += 1
	print(M)

	for dict in dictsList[532*int(length/numero):533*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM532 = np.row_stack((globalFM532,dataArray))
		M += 1
	print(M)

	for dict in dictsList[533*int(length/numero):534*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM533 = np.row_stack((globalFM533,dataArray))
		M += 1
	print(M)

	for dict in dictsList[534*int(length/numero):535*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM534 = np.row_stack((globalFM534,dataArray))
		M += 1
	print(M)

	for dict in dictsList[535*int(length/numero):536*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM535 = np.row_stack((globalFM535,dataArray))
		M += 1
	print(M)

	for dict in dictsList[536*int(length/numero):537*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM536 = np.row_stack((globalFM536,dataArray))
		M += 1
	print(M)

	for dict in dictsList[537*int(length/numero):538*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM537 = np.row_stack((globalFM537,dataArray))
		M += 1
	print(M)

	for dict in dictsList[538*int(length/numero):539*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM538 = np.row_stack((globalFM538,dataArray))
		M += 1
	print(M)

	for dict in dictsList[539*int(length/numero):540*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM539 = np.row_stack((globalFM539,dataArray))
		M += 1
	print(M)

	for dict in dictsList[540*int(length/numero):541*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM540 = np.row_stack((globalFM540,dataArray))
		M += 1
	print(M)

	for dict in dictsList[541*int(length/numero):542*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM541 = np.row_stack((globalFM541,dataArray))
		M += 1
	print(M)

	for dict in dictsList[542*int(length/numero):543*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM542 = np.row_stack((globalFM542,dataArray))
		M += 1
	print(M)

	for dict in dictsList[543*int(length/numero):544*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM543 = np.row_stack((globalFM543,dataArray))
		M += 1
	print(M)

	for dict in dictsList[544*int(length/numero):545*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM544 = np.row_stack((globalFM544,dataArray))
		M += 1
	print(M)

	for dict in dictsList[545*int(length/numero):546*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM545 = np.row_stack((globalFM545,dataArray))
		M += 1
	print(M)

	for dict in dictsList[546*int(length/numero):547*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM546 = np.row_stack((globalFM546,dataArray))
		M += 1
	print(M)

	for dict in dictsList[547*int(length/numero):548*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM547 = np.row_stack((globalFM547,dataArray))
		M += 1
	print(M)

	for dict in dictsList[548*int(length/numero):549*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM548 = np.row_stack((globalFM548,dataArray))
		M += 1
	print(M)

	for dict in dictsList[549*int(length/numero):550*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM549 = np.row_stack((globalFM549,dataArray))
		M += 1
	print(M)

	for dict in dictsList[550*int(length/numero):551*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM550 = np.row_stack((globalFM550,dataArray))
		M += 1
	print(M)

	for dict in dictsList[551*int(length/numero):552*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM551 = np.row_stack((globalFM551,dataArray))
		M += 1
	print(M)

	for dict in dictsList[552*int(length/numero):553*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM552 = np.row_stack((globalFM552,dataArray))
		M += 1
	print(M)

	for dict in dictsList[553*int(length/numero):554*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM553 = np.row_stack((globalFM553,dataArray))
		M += 1
	print(M)

	for dict in dictsList[554*int(length/numero):555*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM554 = np.row_stack((globalFM554,dataArray))
		M += 1
	print(M)

	for dict in dictsList[555*int(length/numero):556*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM555 = np.row_stack((globalFM555,dataArray))
		M += 1
	print(M)

	for dict in dictsList[556*int(length/numero):557*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM556 = np.row_stack((globalFM556,dataArray))
		M += 1
	print(M)

	for dict in dictsList[557*int(length/numero):558*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM557 = np.row_stack((globalFM557,dataArray))
		M += 1
	print(M)

	for dict in dictsList[558*int(length/numero):559*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM558 = np.row_stack((globalFM558,dataArray))
		M += 1
	print(M)

	for dict in dictsList[559*int(length/numero):560*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM559 = np.row_stack((globalFM559,dataArray))
		M += 1
	print(M)

	for dict in dictsList[560*int(length/numero):561*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM560 = np.row_stack((globalFM560,dataArray))
		M += 1
	print(M)

	for dict in dictsList[561*int(length/numero):562*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM561 = np.row_stack((globalFM561,dataArray))
		M += 1
	print(M)

	for dict in dictsList[562*int(length/numero):563*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM562 = np.row_stack((globalFM562,dataArray))
		M += 1
	print(M)

	for dict in dictsList[563*int(length/numero):564*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM563 = np.row_stack((globalFM563,dataArray))
		M += 1
	print(M)

	for dict in dictsList[564*int(length/numero):565*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM564 = np.row_stack((globalFM564,dataArray))
		M += 1
	print(M)

	for dict in dictsList[565*int(length/numero):566*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM565 = np.row_stack((globalFM565,dataArray))
		M += 1
	print(M)

	for dict in dictsList[566*int(length/numero):567*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM566 = np.row_stack((globalFM566,dataArray))
		M += 1
	print(M)

	for dict in dictsList[567*int(length/numero):568*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM567 = np.row_stack((globalFM567,dataArray))
		M += 1
	print(M)

	for dict in dictsList[568*int(length/numero):569*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM568 = np.row_stack((globalFM568,dataArray))
		M += 1
	print(M)

	for dict in dictsList[569*int(length/numero):570*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM569 = np.row_stack((globalFM569,dataArray))
		M += 1
	print(M)

	for dict in dictsList[570*int(length/numero):571*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM570 = np.row_stack((globalFM570,dataArray))
		M += 1
	print(M)

	for dict in dictsList[571*int(length/numero):572*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM571 = np.row_stack((globalFM571,dataArray))
		M += 1
	print(M)

	for dict in dictsList[572*int(length/numero):573*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM572 = np.row_stack((globalFM572,dataArray))
		M += 1
	print(M)

	for dict in dictsList[573*int(length/numero):574*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM573 = np.row_stack((globalFM573,dataArray))
		M += 1
	print(M)

	for dict in dictsList[574*int(length/numero):575*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM574 = np.row_stack((globalFM574,dataArray))
		M += 1
	print(M)

	for dict in dictsList[575*int(length/numero):576*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM575 = np.row_stack((globalFM575,dataArray))
		M += 1
	print(M)

	for dict in dictsList[576*int(length/numero):577*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM576 = np.row_stack((globalFM576,dataArray))
		M += 1
	print(M)

	for dict in dictsList[577*int(length/numero):578*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM577 = np.row_stack((globalFM577,dataArray))
		M += 1
	print(M)

	for dict in dictsList[578*int(length/numero):579*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM578 = np.row_stack((globalFM578,dataArray))
		M += 1
	print(M)

	for dict in dictsList[579*int(length/numero):580*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM579 = np.row_stack((globalFM579,dataArray))
		M += 1
	print(M)

	for dict in dictsList[580*int(length/numero):581*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM580 = np.row_stack((globalFM580,dataArray))
		M += 1
	print(M)

	for dict in dictsList[581*int(length/numero):582*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM581 = np.row_stack((globalFM581,dataArray))
		M += 1
	print(M)

	for dict in dictsList[582*int(length/numero):583*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM582 = np.row_stack((globalFM582,dataArray))
		M += 1
	print(M)

	for dict in dictsList[583*int(length/numero):584*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM583 = np.row_stack((globalFM583,dataArray))
		M += 1
	print(M)

	for dict in dictsList[584*int(length/numero):585*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM584 = np.row_stack((globalFM584,dataArray))
		M += 1
	print(M)

	for dict in dictsList[585*int(length/numero):586*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM585 = np.row_stack((globalFM585,dataArray))
		M += 1
	print(M)

	for dict in dictsList[586*int(length/numero):587*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM586 = np.row_stack((globalFM586,dataArray))
		M += 1
	print(M)

	for dict in dictsList[587*int(length/numero):588*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM587 = np.row_stack((globalFM587,dataArray))
		M += 1
	print(M)

	for dict in dictsList[588*int(length/numero):589*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM588 = np.row_stack((globalFM588,dataArray))
		M += 1
	print(M)

	for dict in dictsList[589*int(length/numero):590*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM589 = np.row_stack((globalFM589,dataArray))
		M += 1
	print(M)

	for dict in dictsList[590*int(length/numero):591*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM590 = np.row_stack((globalFM590,dataArray))
		M += 1
	print(M)

	for dict in dictsList[591*int(length/numero):592*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM591 = np.row_stack((globalFM591,dataArray))
		M += 1
	print(M)

	for dict in dictsList[592*int(length/numero):593*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM592 = np.row_stack((globalFM592,dataArray))
		M += 1
	print(M)

	for dict in dictsList[593*int(length/numero):594*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM593 = np.row_stack((globalFM593,dataArray))
		M += 1
	print(M)

	for dict in dictsList[594*int(length/numero):595*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM594 = np.row_stack((globalFM594,dataArray))
		M += 1
	print(M)

	for dict in dictsList[595*int(length/numero):596*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM595 = np.row_stack((globalFM595,dataArray))
		M += 1
	print(M)

	for dict in dictsList[596*int(length/numero):597*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM596 = np.row_stack((globalFM596,dataArray))
		M += 1
	print(M)

	for dict in dictsList[597*int(length/numero):598*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM597 = np.row_stack((globalFM597,dataArray))
		M += 1
	print(M)

	for dict in dictsList[598*int(length/numero):599*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM598 = np.row_stack((globalFM598,dataArray))
		M += 1
	print(M)

	for dict in dictsList[599*int(length/numero):600*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM599 = np.row_stack((globalFM599,dataArray))
		M += 1
	print(M)

	for dict in dictsList[600*int(length/numero):601*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM600 = np.row_stack((globalFM600,dataArray))
		M += 1
	print(M)

	for dict in dictsList[601*int(length/numero):602*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM601 = np.row_stack((globalFM601,dataArray))
		M += 1
	print(M)

	for dict in dictsList[602*int(length/numero):603*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM602 = np.row_stack((globalFM602,dataArray))
		M += 1
	print(M)

	for dict in dictsList[603*int(length/numero):604*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM603 = np.row_stack((globalFM603,dataArray))
		M += 1
	print(M)

	for dict in dictsList[604*int(length/numero):605*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM604 = np.row_stack((globalFM604,dataArray))
		M += 1
	print(M)

	for dict in dictsList[605*int(length/numero):606*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM605 = np.row_stack((globalFM605,dataArray))
		M += 1
	print(M)

	for dict in dictsList[606*int(length/numero):607*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM606 = np.row_stack((globalFM606,dataArray))
		M += 1
	print(M)

	for dict in dictsList[607*int(length/numero):608*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM607 = np.row_stack((globalFM607,dataArray))
		M += 1
	print(M)

	for dict in dictsList[608*int(length/numero):609*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM608 = np.row_stack((globalFM608,dataArray))
		M += 1
	print(M)

	for dict in dictsList[609*int(length/numero):610*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM609 = np.row_stack((globalFM609,dataArray))
		M += 1
	print(M)

	for dict in dictsList[610*int(length/numero):611*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM610 = np.row_stack((globalFM610,dataArray))
		M += 1
	print(M)

	for dict in dictsList[611*int(length/numero):612*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM611 = np.row_stack((globalFM611,dataArray))
		M += 1
	print(M)

	for dict in dictsList[612*int(length/numero):613*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM612 = np.row_stack((globalFM612,dataArray))
		M += 1
	print(M)

	for dict in dictsList[613*int(length/numero):614*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM613 = np.row_stack((globalFM613,dataArray))
		M += 1
	print(M)

	for dict in dictsList[614*int(length/numero):615*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM614 = np.row_stack((globalFM614,dataArray))
		M += 1
	print(M)

	for dict in dictsList[615*int(length/numero):616*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM615 = np.row_stack((globalFM615,dataArray))
		M += 1
	print(M)

	for dict in dictsList[616*int(length/numero):617*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM616 = np.row_stack((globalFM616,dataArray))
		M += 1
	print(M)

	for dict in dictsList[617*int(length/numero):618*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM617 = np.row_stack((globalFM617,dataArray))
		M += 1
	print(M)

	for dict in dictsList[618*int(length/numero):619*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM618 = np.row_stack((globalFM618,dataArray))
		M += 1
	print(M)

	for dict in dictsList[619*int(length/numero):620*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM619 = np.row_stack((globalFM619,dataArray))
		M += 1
	print(M)

	for dict in dictsList[620*int(length/numero):621*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM620 = np.row_stack((globalFM620,dataArray))
		M += 1
	print(M)

	for dict in dictsList[621*int(length/numero):622*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM621 = np.row_stack((globalFM621,dataArray))
		M += 1
	print(M)

	for dict in dictsList[622*int(length/numero):623*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM622 = np.row_stack((globalFM622,dataArray))
		M += 1
	print(M)

	for dict in dictsList[623*int(length/numero):624*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM623 = np.row_stack((globalFM623,dataArray))
		M += 1
	print(M)

	for dict in dictsList[624*int(length/numero):625*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM624 = np.row_stack((globalFM624,dataArray))
		M += 1
	print(M)

	for dict in dictsList[625*int(length/numero):626*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM625 = np.row_stack((globalFM625,dataArray))
		M += 1
	print(M)

	for dict in dictsList[626*int(length/numero):627*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM626 = np.row_stack((globalFM626,dataArray))
		M += 1
	print(M)

	for dict in dictsList[627*int(length/numero):628*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM627 = np.row_stack((globalFM627,dataArray))
		M += 1
	print(M)

	for dict in dictsList[628*int(length/numero):629*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM628 = np.row_stack((globalFM628,dataArray))
		M += 1
	print(M)

	for dict in dictsList[629*int(length/numero):630*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM629 = np.row_stack((globalFM629,dataArray))
		M += 1
	print(M)

	for dict in dictsList[630*int(length/numero):631*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM630 = np.row_stack((globalFM630,dataArray))
		M += 1
	print(M)

	for dict in dictsList[631*int(length/numero):632*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM631 = np.row_stack((globalFM631,dataArray))
		M += 1
	print(M)

	for dict in dictsList[632*int(length/numero):633*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM632 = np.row_stack((globalFM632,dataArray))
		M += 1
	print(M)

	for dict in dictsList[633*int(length/numero):634*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM633 = np.row_stack((globalFM633,dataArray))
		M += 1
	print(M)

	for dict in dictsList[634*int(length/numero):635*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM634 = np.row_stack((globalFM634,dataArray))
		M += 1
	print(M)

	for dict in dictsList[635*int(length/numero):636*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM635 = np.row_stack((globalFM635,dataArray))
		M += 1
	print(M)

	for dict in dictsList[636*int(length/numero):637*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM636 = np.row_stack((globalFM636,dataArray))
		M += 1
	print(M)

	for dict in dictsList[637*int(length/numero):638*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM637 = np.row_stack((globalFM637,dataArray))
		M += 1
	print(M)

	for dict in dictsList[638*int(length/numero):639*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM638 = np.row_stack((globalFM638,dataArray))
		M += 1
	print(M)

	for dict in dictsList[639*int(length/numero):640*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM639 = np.row_stack((globalFM639,dataArray))
		M += 1
	print(M)

	for dict in dictsList[640*int(length/numero):641*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM640 = np.row_stack((globalFM640,dataArray))
		M += 1
	print(M)

	for dict in dictsList[641*int(length/numero):642*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM641 = np.row_stack((globalFM641,dataArray))
		M += 1
	print(M)

	for dict in dictsList[642*int(length/numero):643*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM642 = np.row_stack((globalFM642,dataArray))
		M += 1
	print(M)

	for dict in dictsList[643*int(length/numero):644*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM643 = np.row_stack((globalFM643,dataArray))
		M += 1
	print(M)

	for dict in dictsList[644*int(length/numero):645*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM644 = np.row_stack((globalFM644,dataArray))
		M += 1
	print(M)

	for dict in dictsList[645*int(length/numero):646*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM645 = np.row_stack((globalFM645,dataArray))
		M += 1
	print(M)

	for dict in dictsList[646*int(length/numero):647*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM646 = np.row_stack((globalFM646,dataArray))
		M += 1
	print(M)

	for dict in dictsList[647*int(length/numero):648*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM647 = np.row_stack((globalFM647,dataArray))
		M += 1
	print(M)

	for dict in dictsList[648*int(length/numero):649*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM648 = np.row_stack((globalFM648,dataArray))
		M += 1
	print(M)

	for dict in dictsList[649*int(length/numero):650*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM649 = np.row_stack((globalFM649,dataArray))
		M += 1
	print(M)

	for dict in dictsList[650*int(length/numero):651*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM650 = np.row_stack((globalFM650,dataArray))
		M += 1
	print(M)

	for dict in dictsList[651*int(length/numero):652*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM651 = np.row_stack((globalFM651,dataArray))
		M += 1
	print(M)

	for dict in dictsList[652*int(length/numero):653*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM652 = np.row_stack((globalFM652,dataArray))
		M += 1
	print(M)

	for dict in dictsList[653*int(length/numero):654*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM653 = np.row_stack((globalFM653,dataArray))
		M += 1
	print(M)

	for dict in dictsList[654*int(length/numero):655*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM654 = np.row_stack((globalFM654,dataArray))
		M += 1
	print(M)

	for dict in dictsList[655*int(length/numero):656*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM655 = np.row_stack((globalFM655,dataArray))
		M += 1
	print(M)

	for dict in dictsList[656*int(length/numero):657*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM656 = np.row_stack((globalFM656,dataArray))
		M += 1
	print(M)

	for dict in dictsList[657*int(length/numero):658*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM657 = np.row_stack((globalFM657,dataArray))
		M += 1
	print(M)

	for dict in dictsList[658*int(length/numero):659*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM658 = np.row_stack((globalFM658,dataArray))
		M += 1
	print(M)

	for dict in dictsList[659*int(length/numero):660*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM659 = np.row_stack((globalFM659,dataArray))
		M += 1
	print(M)

	for dict in dictsList[660*int(length/numero):661*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM660 = np.row_stack((globalFM660,dataArray))
		M += 1
	print(M)

	for dict in dictsList[661*int(length/numero):662*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM661 = np.row_stack((globalFM661,dataArray))
		M += 1
	print(M)

	for dict in dictsList[662*int(length/numero):663*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM662 = np.row_stack((globalFM662,dataArray))
		M += 1
	print(M)

	for dict in dictsList[663*int(length/numero):664*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM663 = np.row_stack((globalFM663,dataArray))
		M += 1
	print(M)

	for dict in dictsList[664*int(length/numero):665*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM664 = np.row_stack((globalFM664,dataArray))
		M += 1
	print(M)

	for dict in dictsList[665*int(length/numero):666*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM665 = np.row_stack((globalFM665,dataArray))
		M += 1
	print(M)

	for dict in dictsList[666*int(length/numero):667*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM666 = np.row_stack((globalFM666,dataArray))
		M += 1
	print(M)

	for dict in dictsList[667*int(length/numero):668*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM667 = np.row_stack((globalFM667,dataArray))
		M += 1
	print(M)

	for dict in dictsList[668*int(length/numero):669*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM668 = np.row_stack((globalFM668,dataArray))
		M += 1
	print(M)

	for dict in dictsList[669*int(length/numero):670*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM669 = np.row_stack((globalFM669,dataArray))
		M += 1
	print(M)

	for dict in dictsList[670*int(length/numero):671*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM670 = np.row_stack((globalFM670,dataArray))
		M += 1
	print(M)

	for dict in dictsList[671*int(length/numero):672*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM671 = np.row_stack((globalFM671,dataArray))
		M += 1
	print(M)

	for dict in dictsList[672*int(length/numero):673*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM672 = np.row_stack((globalFM672,dataArray))
		M += 1
	print(M)

	for dict in dictsList[673*int(length/numero):674*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM673 = np.row_stack((globalFM673,dataArray))
		M += 1
	print(M)

	for dict in dictsList[674*int(length/numero):675*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM674 = np.row_stack((globalFM674,dataArray))
		M += 1
	print(M)

	for dict in dictsList[675*int(length/numero):676*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM675 = np.row_stack((globalFM675,dataArray))
		M += 1
	print(M)

	for dict in dictsList[676*int(length/numero):677*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM676 = np.row_stack((globalFM676,dataArray))
		M += 1
	print(M)

	for dict in dictsList[677*int(length/numero):678*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM677 = np.row_stack((globalFM677,dataArray))
		M += 1
	print(M)

	for dict in dictsList[678*int(length/numero):679*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM678 = np.row_stack((globalFM678,dataArray))
		M += 1
	print(M)

	for dict in dictsList[679*int(length/numero):680*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM679 = np.row_stack((globalFM679,dataArray))
		M += 1
	print(M)

	for dict in dictsList[680*int(length/numero):681*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM680 = np.row_stack((globalFM680,dataArray))
		M += 1
	print(M)

	for dict in dictsList[681*int(length/numero):682*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM681 = np.row_stack((globalFM681,dataArray))
		M += 1
	print(M)

	for dict in dictsList[682*int(length/numero):683*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM682 = np.row_stack((globalFM682,dataArray))
		M += 1
	print(M)

	for dict in dictsList[683*int(length/numero):684*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM683 = np.row_stack((globalFM683,dataArray))
		M += 1
	print(M)

	for dict in dictsList[684*int(length/numero):685*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM684 = np.row_stack((globalFM684,dataArray))
		M += 1
	print(M)

	for dict in dictsList[685*int(length/numero):686*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM685 = np.row_stack((globalFM685,dataArray))
		M += 1
	print(M)

	for dict in dictsList[686*int(length/numero):687*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM686 = np.row_stack((globalFM686,dataArray))
		M += 1
	print(M)

	for dict in dictsList[687*int(length/numero):688*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM687 = np.row_stack((globalFM687,dataArray))
		M += 1
	print(M)

	for dict in dictsList[688*int(length/numero):689*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM688 = np.row_stack((globalFM688,dataArray))
		M += 1
	print(M)

	for dict in dictsList[689*int(length/numero):690*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM689 = np.row_stack((globalFM689,dataArray))
		M += 1
	print(M)

	for dict in dictsList[690*int(length/numero):691*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM690 = np.row_stack((globalFM690,dataArray))
		M += 1
	print(M)

	for dict in dictsList[691*int(length/numero):692*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM691 = np.row_stack((globalFM691,dataArray))
		M += 1
	print(M)

	for dict in dictsList[692*int(length/numero):693*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM692 = np.row_stack((globalFM692,dataArray))
		M += 1
	print(M)

	for dict in dictsList[693*int(length/numero):694*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM693 = np.row_stack((globalFM693,dataArray))
		M += 1
	print(M)

	for dict in dictsList[694*int(length/numero):695*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM694 = np.row_stack((globalFM694,dataArray))
		M += 1
	print(M)

	for dict in dictsList[695*int(length/numero):696*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM695 = np.row_stack((globalFM695,dataArray))
		M += 1
	print(M)

	for dict in dictsList[696*int(length/numero):697*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM696 = np.row_stack((globalFM696,dataArray))
		M += 1
	print(M)

	for dict in dictsList[697*int(length/numero):698*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM697 = np.row_stack((globalFM697,dataArray))
		M += 1
	print(M)

	for dict in dictsList[698*int(length/numero):699*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM698 = np.row_stack((globalFM698,dataArray))
		M += 1
	print(M)

	for dict in dictsList[699*int(length/numero):700*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM699 = np.row_stack((globalFM699,dataArray))
		M += 1
	print(M)

	for dict in dictsList[700*int(length/numero):701*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM700 = np.row_stack((globalFM700,dataArray))
		M += 1
	print(M)

	for dict in dictsList[701*int(length/numero):702*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM701 = np.row_stack((globalFM701,dataArray))
		M += 1
	print(M)

	for dict in dictsList[702*int(length/numero):703*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM702 = np.row_stack((globalFM702,dataArray))
		M += 1
	print(M)

	for dict in dictsList[703*int(length/numero):704*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM703 = np.row_stack((globalFM703,dataArray))
		M += 1
	print(M)

	for dict in dictsList[704*int(length/numero):705*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM704 = np.row_stack((globalFM704,dataArray))
		M += 1
	print(M)

	for dict in dictsList[705*int(length/numero):706*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM705 = np.row_stack((globalFM705,dataArray))
		M += 1
	print(M)

	for dict in dictsList[706*int(length/numero):707*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM706 = np.row_stack((globalFM706,dataArray))
		M += 1
	print(M)

	for dict in dictsList[707*int(length/numero):708*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM707 = np.row_stack((globalFM707,dataArray))
		M += 1
	print(M)

	for dict in dictsList[708*int(length/numero):709*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM708 = np.row_stack((globalFM708,dataArray))
		M += 1
	print(M)

	for dict in dictsList[709*int(length/numero):710*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM709 = np.row_stack((globalFM709,dataArray))
		M += 1
	print(M)

	for dict in dictsList[710*int(length/numero):711*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM710 = np.row_stack((globalFM710,dataArray))
		M += 1
	print(M)

	for dict in dictsList[711*int(length/numero):712*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM711 = np.row_stack((globalFM711,dataArray))
		M += 1
	print(M)

	for dict in dictsList[712*int(length/numero):713*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM712 = np.row_stack((globalFM712,dataArray))
		M += 1
	print(M)

	for dict in dictsList[713*int(length/numero):714*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM713 = np.row_stack((globalFM713,dataArray))
		M += 1
	print(M)

	for dict in dictsList[714*int(length/numero):715*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM714 = np.row_stack((globalFM714,dataArray))
		M += 1
	print(M)

	for dict in dictsList[715*int(length/numero):716*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM715 = np.row_stack((globalFM715,dataArray))
		M += 1
	print(M)

	for dict in dictsList[716*int(length/numero):717*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM716 = np.row_stack((globalFM716,dataArray))
		M += 1
	print(M)

	for dict in dictsList[717*int(length/numero):718*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM717 = np.row_stack((globalFM717,dataArray))
		M += 1
	print(M)

	for dict in dictsList[718*int(length/numero):719*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM718 = np.row_stack((globalFM718,dataArray))
		M += 1
	print(M)

	for dict in dictsList[719*int(length/numero):720*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM719 = np.row_stack((globalFM719,dataArray))
		M += 1
	print(M)

	for dict in dictsList[720*int(length/numero):721*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM720 = np.row_stack((globalFM720,dataArray))
		M += 1
	print(M)

	for dict in dictsList[721*int(length/numero):722*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM721 = np.row_stack((globalFM721,dataArray))
		M += 1
	print(M)

	for dict in dictsList[722*int(length/numero):723*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM722 = np.row_stack((globalFM722,dataArray))
		M += 1
	print(M)

	for dict in dictsList[723*int(length/numero):724*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM723 = np.row_stack((globalFM723,dataArray))
		M += 1
	print(M)

	for dict in dictsList[724*int(length/numero):725*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM724 = np.row_stack((globalFM724,dataArray))
		M += 1
	print(M)

	for dict in dictsList[725*int(length/numero):726*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM725 = np.row_stack((globalFM725,dataArray))
		M += 1
	print(M)

	for dict in dictsList[726*int(length/numero):727*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM726 = np.row_stack((globalFM726,dataArray))
		M += 1
	print(M)

	for dict in dictsList[727*int(length/numero):728*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM727 = np.row_stack((globalFM727,dataArray))
		M += 1
	print(M)

	for dict in dictsList[728*int(length/numero):729*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM728 = np.row_stack((globalFM728,dataArray))
		M += 1
	print(M)

	for dict in dictsList[729*int(length/numero):730*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM729 = np.row_stack((globalFM729,dataArray))
		M += 1
	print(M)

	for dict in dictsList[730*int(length/numero):731*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM730 = np.row_stack((globalFM730,dataArray))
		M += 1
	print(M)

	for dict in dictsList[731*int(length/numero):732*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM731 = np.row_stack((globalFM731,dataArray))
		M += 1
	print(M)

	for dict in dictsList[732*int(length/numero):733*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM732 = np.row_stack((globalFM732,dataArray))
		M += 1
	print(M)

	for dict in dictsList[733*int(length/numero):734*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM733 = np.row_stack((globalFM733,dataArray))
		M += 1
	print(M)

	for dict in dictsList[734*int(length/numero):735*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM734 = np.row_stack((globalFM734,dataArray))
		M += 1
	print(M)

	for dict in dictsList[735*int(length/numero):736*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM735 = np.row_stack((globalFM735,dataArray))
		M += 1
	print(M)

	for dict in dictsList[736*int(length/numero):737*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM736 = np.row_stack((globalFM736,dataArray))
		M += 1
	print(M)

	for dict in dictsList[737*int(length/numero):738*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM737 = np.row_stack((globalFM737,dataArray))
		M += 1
	print(M)

	for dict in dictsList[738*int(length/numero):739*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM738 = np.row_stack((globalFM738,dataArray))
		M += 1
	print(M)

	for dict in dictsList[739*int(length/numero):740*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM739 = np.row_stack((globalFM739,dataArray))
		M += 1
	print(M)

	for dict in dictsList[740*int(length/numero):741*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM740 = np.row_stack((globalFM740,dataArray))
		M += 1
	print(M)

	for dict in dictsList[741*int(length/numero):742*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM741 = np.row_stack((globalFM741,dataArray))
		M += 1
	print(M)

	for dict in dictsList[742*int(length/numero):743*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM742 = np.row_stack((globalFM742,dataArray))
		M += 1
	print(M)

	for dict in dictsList[743*int(length/numero):744*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM743 = np.row_stack((globalFM743,dataArray))
		M += 1
	print(M)

	for dict in dictsList[744*int(length/numero):745*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM744 = np.row_stack((globalFM744,dataArray))
		M += 1
	print(M)

	for dict in dictsList[745*int(length/numero):746*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM745 = np.row_stack((globalFM745,dataArray))
		M += 1
	print(M)

	for dict in dictsList[746*int(length/numero):747*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM746 = np.row_stack((globalFM746,dataArray))
		M += 1
	print(M)

	for dict in dictsList[747*int(length/numero):748*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM747 = np.row_stack((globalFM747,dataArray))
		M += 1
	print(M)

	for dict in dictsList[748*int(length/numero):749*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM748 = np.row_stack((globalFM748,dataArray))
		M += 1
	print(M)

	for dict in dictsList[749*int(length/numero):750*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM749 = np.row_stack((globalFM749,dataArray))
		M += 1
	print(M)

	for dict in dictsList[750*int(length/numero):751*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM750 = np.row_stack((globalFM750,dataArray))
		M += 1
	print(M)

	for dict in dictsList[751*int(length/numero):752*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM751 = np.row_stack((globalFM751,dataArray))
		M += 1
	print(M)

	for dict in dictsList[752*int(length/numero):753*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM752 = np.row_stack((globalFM752,dataArray))
		M += 1
	print(M)

	for dict in dictsList[753*int(length/numero):754*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM753 = np.row_stack((globalFM753,dataArray))
		M += 1
	print(M)

	for dict in dictsList[754*int(length/numero):755*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM754 = np.row_stack((globalFM754,dataArray))
		M += 1
	print(M)

	for dict in dictsList[755*int(length/numero):756*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM755 = np.row_stack((globalFM755,dataArray))
		M += 1
	print(M)

	for dict in dictsList[756*int(length/numero):757*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM756 = np.row_stack((globalFM756,dataArray))
		M += 1
	print(M)

	for dict in dictsList[757*int(length/numero):758*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM757 = np.row_stack((globalFM757,dataArray))
		M += 1
	print(M)

	for dict in dictsList[758*int(length/numero):759*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM758 = np.row_stack((globalFM758,dataArray))
		M += 1
	print(M)

	for dict in dictsList[759*int(length/numero):760*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM759 = np.row_stack((globalFM759,dataArray))
		M += 1
	print(M)

	for dict in dictsList[760*int(length/numero):761*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM760 = np.row_stack((globalFM760,dataArray))
		M += 1
	print(M)

	for dict in dictsList[761*int(length/numero):762*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM761 = np.row_stack((globalFM761,dataArray))
		M += 1
	print(M)

	for dict in dictsList[762*int(length/numero):763*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM762 = np.row_stack((globalFM762,dataArray))
		M += 1
	print(M)

	for dict in dictsList[763*int(length/numero):764*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM763 = np.row_stack((globalFM763,dataArray))
		M += 1
	print(M)

	for dict in dictsList[764*int(length/numero):765*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM764 = np.row_stack((globalFM764,dataArray))
		M += 1
	print(M)

	for dict in dictsList[765*int(length/numero):766*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM765 = np.row_stack((globalFM765,dataArray))
		M += 1
	print(M)

	for dict in dictsList[766*int(length/numero):767*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM766 = np.row_stack((globalFM766,dataArray))
		M += 1
	print(M)

	for dict in dictsList[767*int(length/numero):768*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM767 = np.row_stack((globalFM767,dataArray))
		M += 1
	print(M)

	for dict in dictsList[768*int(length/numero):769*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM768 = np.row_stack((globalFM768,dataArray))
		M += 1
	print(M)

	for dict in dictsList[769*int(length/numero):770*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM769 = np.row_stack((globalFM769,dataArray))
		M += 1
	print(M)

	for dict in dictsList[770*int(length/numero):771*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM770 = np.row_stack((globalFM770,dataArray))
		M += 1
	print(M)

	for dict in dictsList[771*int(length/numero):772*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM771 = np.row_stack((globalFM771,dataArray))
		M += 1
	print(M)

	for dict in dictsList[772*int(length/numero):773*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM772 = np.row_stack((globalFM772,dataArray))
		M += 1
	print(M)

	for dict in dictsList[773*int(length/numero):774*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM773 = np.row_stack((globalFM773,dataArray))
		M += 1
	print(M)

	for dict in dictsList[774*int(length/numero):775*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM774 = np.row_stack((globalFM774,dataArray))
		M += 1
	print(M)

	for dict in dictsList[775*int(length/numero):776*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM775 = np.row_stack((globalFM775,dataArray))
		M += 1
	print(M)

	for dict in dictsList[776*int(length/numero):777*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM776 = np.row_stack((globalFM776,dataArray))
		M += 1
	print(M)

	for dict in dictsList[777*int(length/numero):778*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM777 = np.row_stack((globalFM777,dataArray))
		M += 1
	print(M)

	for dict in dictsList[778*int(length/numero):779*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM778 = np.row_stack((globalFM778,dataArray))
		M += 1
	print(M)

	for dict in dictsList[779*int(length/numero):780*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM779 = np.row_stack((globalFM779,dataArray))
		M += 1
	print(M)

	for dict in dictsList[780*int(length/numero):781*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM780 = np.row_stack((globalFM780,dataArray))
		M += 1
	print(M)

	for dict in dictsList[781*int(length/numero):782*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM781 = np.row_stack((globalFM781,dataArray))
		M += 1
	print(M)

	for dict in dictsList[782*int(length/numero):783*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM782 = np.row_stack((globalFM782,dataArray))
		M += 1
	print(M)

	for dict in dictsList[783*int(length/numero):784*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM783 = np.row_stack((globalFM783,dataArray))
		M += 1
	print(M)

	for dict in dictsList[784*int(length/numero):785*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM784 = np.row_stack((globalFM784,dataArray))
		M += 1
	print(M)

	for dict in dictsList[785*int(length/numero):786*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM785 = np.row_stack((globalFM785,dataArray))
		M += 1
	print(M)

	for dict in dictsList[786*int(length/numero):787*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM786 = np.row_stack((globalFM786,dataArray))
		M += 1
	print(M)

	for dict in dictsList[787*int(length/numero):788*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM787 = np.row_stack((globalFM787,dataArray))
		M += 1
	print(M)

	for dict in dictsList[788*int(length/numero):789*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM788 = np.row_stack((globalFM788,dataArray))
		M += 1
	print(M)

	for dict in dictsList[789*int(length/numero):790*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM789 = np.row_stack((globalFM789,dataArray))
		M += 1
	print(M)

	for dict in dictsList[790*int(length/numero):791*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM790 = np.row_stack((globalFM790,dataArray))
		M += 1
	print(M)

	for dict in dictsList[791*int(length/numero):792*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM791 = np.row_stack((globalFM791,dataArray))
		M += 1
	print(M)

	for dict in dictsList[792*int(length/numero):793*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM792 = np.row_stack((globalFM792,dataArray))
		M += 1
	print(M)

	for dict in dictsList[793*int(length/numero):794*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM793 = np.row_stack((globalFM793,dataArray))
		M += 1
	print(M)

	for dict in dictsList[794*int(length/numero):795*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM794 = np.row_stack((globalFM794,dataArray))
		M += 1
	print(M)

	for dict in dictsList[795*int(length/numero):796*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM795 = np.row_stack((globalFM795,dataArray))
		M += 1
	print(M)

	for dict in dictsList[796*int(length/numero):797*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM796 = np.row_stack((globalFM796,dataArray))
		M += 1
	print(M)

	for dict in dictsList[797*int(length/numero):798*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM797 = np.row_stack((globalFM797,dataArray))
		M += 1
	print(M)

	for dict in dictsList[798*int(length/numero):799*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM798 = np.row_stack((globalFM798,dataArray))
		M += 1
	print(M)

	for dict in dictsList[799*int(length/numero):800*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM799 = np.row_stack((globalFM799,dataArray))
		M += 1
	print(M)

	for dict in dictsList[800*int(length/numero):801*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM800 = np.row_stack((globalFM800,dataArray))
		M += 1
	print(M)

	for dict in dictsList[801*int(length/numero):802*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM801 = np.row_stack((globalFM801,dataArray))
		M += 1
	print(M)

	for dict in dictsList[802*int(length/numero):803*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM802 = np.row_stack((globalFM802,dataArray))
		M += 1
	print(M)

	for dict in dictsList[803*int(length/numero):804*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM803 = np.row_stack((globalFM803,dataArray))
		M += 1
	print(M)

	for dict in dictsList[804*int(length/numero):805*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM804 = np.row_stack((globalFM804,dataArray))
		M += 1
	print(M)

	for dict in dictsList[805*int(length/numero):806*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM805 = np.row_stack((globalFM805,dataArray))
		M += 1
	print(M)

	for dict in dictsList[806*int(length/numero):807*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM806 = np.row_stack((globalFM806,dataArray))
		M += 1
	print(M)

	for dict in dictsList[807*int(length/numero):808*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM807 = np.row_stack((globalFM807,dataArray))
		M += 1
	print(M)

	for dict in dictsList[808*int(length/numero):809*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM808 = np.row_stack((globalFM808,dataArray))
		M += 1
	print(M)

	for dict in dictsList[809*int(length/numero):810*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM809 = np.row_stack((globalFM809,dataArray))
		M += 1
	print(M)

	for dict in dictsList[810*int(length/numero):811*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM810 = np.row_stack((globalFM810,dataArray))
		M += 1
	print(M)

	for dict in dictsList[811*int(length/numero):812*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM811 = np.row_stack((globalFM811,dataArray))
		M += 1
	print(M)

	for dict in dictsList[812*int(length/numero):813*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM812 = np.row_stack((globalFM812,dataArray))
		M += 1
	print(M)

	for dict in dictsList[813*int(length/numero):814*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM813 = np.row_stack((globalFM813,dataArray))
		M += 1
	print(M)

	for dict in dictsList[814*int(length/numero):815*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM814 = np.row_stack((globalFM814,dataArray))
		M += 1
	print(M)

	for dict in dictsList[815*int(length/numero):816*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM815 = np.row_stack((globalFM815,dataArray))
		M += 1
	print(M)

	for dict in dictsList[816*int(length/numero):817*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM816 = np.row_stack((globalFM816,dataArray))
		M += 1
	print(M)

	for dict in dictsList[817*int(length/numero):818*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM817 = np.row_stack((globalFM817,dataArray))
		M += 1
	print(M)

	for dict in dictsList[818*int(length/numero):819*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM818 = np.row_stack((globalFM818,dataArray))
		M += 1
	print(M)

	for dict in dictsList[819*int(length/numero):820*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM819 = np.row_stack((globalFM819,dataArray))
		M += 1
	print(M)

	for dict in dictsList[820*int(length/numero):821*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM820 = np.row_stack((globalFM820,dataArray))
		M += 1
	print(M)

	for dict in dictsList[821*int(length/numero):822*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM821 = np.row_stack((globalFM821,dataArray))
		M += 1
	print(M)

	for dict in dictsList[822*int(length/numero):823*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM822 = np.row_stack((globalFM822,dataArray))
		M += 1
	print(M)

	for dict in dictsList[823*int(length/numero):824*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM823 = np.row_stack((globalFM823,dataArray))
		M += 1
	print(M)

	for dict in dictsList[824*int(length/numero):825*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM824 = np.row_stack((globalFM824,dataArray))
		M += 1
	print(M)

	for dict in dictsList[825*int(length/numero):826*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM825 = np.row_stack((globalFM825,dataArray))
		M += 1
	print(M)

	for dict in dictsList[826*int(length/numero):827*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM826 = np.row_stack((globalFM826,dataArray))
		M += 1
	print(M)

	for dict in dictsList[827*int(length/numero):828*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM827 = np.row_stack((globalFM827,dataArray))
		M += 1
	print(M)

	for dict in dictsList[828*int(length/numero):829*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM828 = np.row_stack((globalFM828,dataArray))
		M += 1
	print(M)

	for dict in dictsList[829*int(length/numero):830*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM829 = np.row_stack((globalFM829,dataArray))
		M += 1
	print(M)

	for dict in dictsList[830*int(length/numero):831*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM830 = np.row_stack((globalFM830,dataArray))
		M += 1
	print(M)

	for dict in dictsList[831*int(length/numero):832*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM831 = np.row_stack((globalFM831,dataArray))
		M += 1
	print(M)

	for dict in dictsList[832*int(length/numero):833*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM832 = np.row_stack((globalFM832,dataArray))
		M += 1
	print(M)

	for dict in dictsList[833*int(length/numero):834*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM833 = np.row_stack((globalFM833,dataArray))
		M += 1
	print(M)

	for dict in dictsList[834*int(length/numero):835*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM834 = np.row_stack((globalFM834,dataArray))
		M += 1
	print(M)

	for dict in dictsList[835*int(length/numero):836*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM835 = np.row_stack((globalFM835,dataArray))
		M += 1
	print(M)

	for dict in dictsList[836*int(length/numero):837*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM836 = np.row_stack((globalFM836,dataArray))
		M += 1
	print(M)

	for dict in dictsList[837*int(length/numero):838*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM837 = np.row_stack((globalFM837,dataArray))
		M += 1
	print(M)

	for dict in dictsList[838*int(length/numero):839*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM838 = np.row_stack((globalFM838,dataArray))
		M += 1
	print(M)

	for dict in dictsList[839*int(length/numero):840*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM839 = np.row_stack((globalFM839,dataArray))
		M += 1
	print(M)

	for dict in dictsList[840*int(length/numero):841*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM840 = np.row_stack((globalFM840,dataArray))
		M += 1
	print(M)

	for dict in dictsList[841*int(length/numero):842*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM841 = np.row_stack((globalFM841,dataArray))
		M += 1
	print(M)

	for dict in dictsList[842*int(length/numero):843*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM842 = np.row_stack((globalFM842,dataArray))
		M += 1
	print(M)

	for dict in dictsList[843*int(length/numero):844*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM843 = np.row_stack((globalFM843,dataArray))
		M += 1
	print(M)

	for dict in dictsList[844*int(length/numero):845*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM844 = np.row_stack((globalFM844,dataArray))
		M += 1
	print(M)

	for dict in dictsList[845*int(length/numero):846*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM845 = np.row_stack((globalFM845,dataArray))
		M += 1
	print(M)

	for dict in dictsList[846*int(length/numero):847*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM846 = np.row_stack((globalFM846,dataArray))
		M += 1
	print(M)

	for dict in dictsList[847*int(length/numero):848*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM847 = np.row_stack((globalFM847,dataArray))
		M += 1
	print(M)

	for dict in dictsList[848*int(length/numero):849*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM848 = np.row_stack((globalFM848,dataArray))
		M += 1
	print(M)

	for dict in dictsList[849*int(length/numero):850*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM849 = np.row_stack((globalFM849,dataArray))
		M += 1
	print(M)

	for dict in dictsList[850*int(length/numero):851*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM850 = np.row_stack((globalFM850,dataArray))
		M += 1
	print(M)

	for dict in dictsList[851*int(length/numero):852*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM851 = np.row_stack((globalFM851,dataArray))
		M += 1
	print(M)

	for dict in dictsList[852*int(length/numero):853*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM852 = np.row_stack((globalFM852,dataArray))
		M += 1
	print(M)

	for dict in dictsList[853*int(length/numero):854*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM853 = np.row_stack((globalFM853,dataArray))
		M += 1
	print(M)

	for dict in dictsList[854*int(length/numero):855*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM854 = np.row_stack((globalFM854,dataArray))
		M += 1
	print(M)

	for dict in dictsList[855*int(length/numero):856*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM855 = np.row_stack((globalFM855,dataArray))
		M += 1
	print(M)

	for dict in dictsList[856*int(length/numero):857*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM856 = np.row_stack((globalFM856,dataArray))
		M += 1
	print(M)

	for dict in dictsList[857*int(length/numero):858*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM857 = np.row_stack((globalFM857,dataArray))
		M += 1
	print(M)

	for dict in dictsList[858*int(length/numero):859*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM858 = np.row_stack((globalFM858,dataArray))
		M += 1
	print(M)

	for dict in dictsList[859*int(length/numero):860*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM859 = np.row_stack((globalFM859,dataArray))
		M += 1
	print(M)

	for dict in dictsList[860*int(length/numero):861*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM860 = np.row_stack((globalFM860,dataArray))
		M += 1
	print(M)

	for dict in dictsList[861*int(length/numero):862*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM861 = np.row_stack((globalFM861,dataArray))
		M += 1
	print(M)

	for dict in dictsList[862*int(length/numero):863*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM862 = np.row_stack((globalFM862,dataArray))
		M += 1
	print(M)

	for dict in dictsList[863*int(length/numero):864*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM863 = np.row_stack((globalFM863,dataArray))
		M += 1
	print(M)

	for dict in dictsList[864*int(length/numero):865*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM864 = np.row_stack((globalFM864,dataArray))
		M += 1
	print(M)

	for dict in dictsList[865*int(length/numero):866*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM865 = np.row_stack((globalFM865,dataArray))
		M += 1
	print(M)

	for dict in dictsList[866*int(length/numero):867*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM866 = np.row_stack((globalFM866,dataArray))
		M += 1
	print(M)

	for dict in dictsList[867*int(length/numero):868*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM867 = np.row_stack((globalFM867,dataArray))
		M += 1
	print(M)

	for dict in dictsList[868*int(length/numero):869*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM868 = np.row_stack((globalFM868,dataArray))
		M += 1
	print(M)

	for dict in dictsList[869*int(length/numero):870*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM869 = np.row_stack((globalFM869,dataArray))
		M += 1
	print(M)

	for dict in dictsList[870*int(length/numero):871*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM870 = np.row_stack((globalFM870,dataArray))
		M += 1
	print(M)

	for dict in dictsList[871*int(length/numero):872*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM871 = np.row_stack((globalFM871,dataArray))
		M += 1
	print(M)

	for dict in dictsList[872*int(length/numero):873*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM872 = np.row_stack((globalFM872,dataArray))
		M += 1
	print(M)

	for dict in dictsList[873*int(length/numero):874*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM873 = np.row_stack((globalFM873,dataArray))
		M += 1
	print(M)

	for dict in dictsList[874*int(length/numero):875*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM874 = np.row_stack((globalFM874,dataArray))
		M += 1
	print(M)

	for dict in dictsList[875*int(length/numero):876*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM875 = np.row_stack((globalFM875,dataArray))
		M += 1
	print(M)

	for dict in dictsList[876*int(length/numero):877*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM876 = np.row_stack((globalFM876,dataArray))
		M += 1
	print(M)

	for dict in dictsList[877*int(length/numero):878*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM877 = np.row_stack((globalFM877,dataArray))
		M += 1
	print(M)

	for dict in dictsList[878*int(length/numero):879*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM878 = np.row_stack((globalFM878,dataArray))
		M += 1
	print(M)

	for dict in dictsList[879*int(length/numero):880*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM879 = np.row_stack((globalFM879,dataArray))
		M += 1
	print(M)

	for dict in dictsList[880*int(length/numero):881*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM880 = np.row_stack((globalFM880,dataArray))
		M += 1
	print(M)

	for dict in dictsList[881*int(length/numero):882*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM881 = np.row_stack((globalFM881,dataArray))
		M += 1
	print(M)

	for dict in dictsList[882*int(length/numero):883*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM882 = np.row_stack((globalFM882,dataArray))
		M += 1
	print(M)

	for dict in dictsList[883*int(length/numero):884*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM883 = np.row_stack((globalFM883,dataArray))
		M += 1
	print(M)

	for dict in dictsList[884*int(length/numero):885*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM884 = np.row_stack((globalFM884,dataArray))
		M += 1
	print(M)

	for dict in dictsList[885*int(length/numero):886*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM885 = np.row_stack((globalFM885,dataArray))
		M += 1
	print(M)

	for dict in dictsList[886*int(length/numero):887*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM886 = np.row_stack((globalFM886,dataArray))
		M += 1
	print(M)

	for dict in dictsList[887*int(length/numero):888*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM887 = np.row_stack((globalFM887,dataArray))
		M += 1
	print(M)

	for dict in dictsList[888*int(length/numero):889*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM888 = np.row_stack((globalFM888,dataArray))
		M += 1
	print(M)

	for dict in dictsList[889*int(length/numero):890*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM889 = np.row_stack((globalFM889,dataArray))
		M += 1
	print(M)

	for dict in dictsList[890*int(length/numero):891*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM890 = np.row_stack((globalFM890,dataArray))
		M += 1
	print(M)

	for dict in dictsList[891*int(length/numero):892*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM891 = np.row_stack((globalFM891,dataArray))
		M += 1
	print(M)

	for dict in dictsList[892*int(length/numero):893*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM892 = np.row_stack((globalFM892,dataArray))
		M += 1
	print(M)

	for dict in dictsList[893*int(length/numero):894*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM893 = np.row_stack((globalFM893,dataArray))
		M += 1
	print(M)

	for dict in dictsList[894*int(length/numero):895*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM894 = np.row_stack((globalFM894,dataArray))
		M += 1
	print(M)

	for dict in dictsList[895*int(length/numero):896*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM895 = np.row_stack((globalFM895,dataArray))
		M += 1
	print(M)

	for dict in dictsList[896*int(length/numero):897*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM896 = np.row_stack((globalFM896,dataArray))
		M += 1
	print(M)

	for dict in dictsList[897*int(length/numero):898*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM897 = np.row_stack((globalFM897,dataArray))
		M += 1
	print(M)

	for dict in dictsList[898*int(length/numero):899*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM898 = np.row_stack((globalFM898,dataArray))
		M += 1
	print(M)

	for dict in dictsList[899*int(length/numero):900*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM899 = np.row_stack((globalFM899,dataArray))
		M += 1
	print(M)

	for dict in dictsList[900*int(length/numero):901*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM900 = np.row_stack((globalFM900,dataArray))
		M += 1
	print(M)

	for dict in dictsList[901*int(length/numero):902*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM901 = np.row_stack((globalFM901,dataArray))
		M += 1
	print(M)

	for dict in dictsList[902*int(length/numero):903*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM902 = np.row_stack((globalFM902,dataArray))
		M += 1
	print(M)

	for dict in dictsList[903*int(length/numero):904*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM903 = np.row_stack((globalFM903,dataArray))
		M += 1
	print(M)

	for dict in dictsList[904*int(length/numero):905*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM904 = np.row_stack((globalFM904,dataArray))
		M += 1
	print(M)

	for dict in dictsList[905*int(length/numero):906*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM905 = np.row_stack((globalFM905,dataArray))
		M += 1
	print(M)

	for dict in dictsList[906*int(length/numero):907*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM906 = np.row_stack((globalFM906,dataArray))
		M += 1
	print(M)

	for dict in dictsList[907*int(length/numero):908*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM907 = np.row_stack((globalFM907,dataArray))
		M += 1
	print(M)

	for dict in dictsList[908*int(length/numero):909*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM908 = np.row_stack((globalFM908,dataArray))
		M += 1
	print(M)

	for dict in dictsList[909*int(length/numero):910*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM909 = np.row_stack((globalFM909,dataArray))
		M += 1
	print(M)

	for dict in dictsList[910*int(length/numero):911*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM910 = np.row_stack((globalFM910,dataArray))
		M += 1
	print(M)

	for dict in dictsList[911*int(length/numero):912*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM911 = np.row_stack((globalFM911,dataArray))
		M += 1
	print(M)

	for dict in dictsList[912*int(length/numero):913*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM912 = np.row_stack((globalFM912,dataArray))
		M += 1
	print(M)

	for dict in dictsList[913*int(length/numero):914*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM913 = np.row_stack((globalFM913,dataArray))
		M += 1
	print(M)

	for dict in dictsList[914*int(length/numero):915*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM914 = np.row_stack((globalFM914,dataArray))
		M += 1
	print(M)

	for dict in dictsList[915*int(length/numero):916*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM915 = np.row_stack((globalFM915,dataArray))
		M += 1
	print(M)

	for dict in dictsList[916*int(length/numero):917*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM916 = np.row_stack((globalFM916,dataArray))
		M += 1
	print(M)

	for dict in dictsList[917*int(length/numero):918*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM917 = np.row_stack((globalFM917,dataArray))
		M += 1
	print(M)

	for dict in dictsList[918*int(length/numero):919*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM918 = np.row_stack((globalFM918,dataArray))
		M += 1
	print(M)

	for dict in dictsList[919*int(length/numero):920*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM919 = np.row_stack((globalFM919,dataArray))
		M += 1
	print(M)

	for dict in dictsList[920*int(length/numero):921*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM920 = np.row_stack((globalFM920,dataArray))
		M += 1
	print(M)

	for dict in dictsList[921*int(length/numero):922*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM921 = np.row_stack((globalFM921,dataArray))
		M += 1
	print(M)

	for dict in dictsList[922*int(length/numero):923*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM922 = np.row_stack((globalFM922,dataArray))
		M += 1
	print(M)

	for dict in dictsList[923*int(length/numero):924*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM923 = np.row_stack((globalFM923,dataArray))
		M += 1
	print(M)

	for dict in dictsList[924*int(length/numero):925*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM924 = np.row_stack((globalFM924,dataArray))
		M += 1
	print(M)

	for dict in dictsList[925*int(length/numero):926*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM925 = np.row_stack((globalFM925,dataArray))
		M += 1
	print(M)

	for dict in dictsList[926*int(length/numero):927*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM926 = np.row_stack((globalFM926,dataArray))
		M += 1
	print(M)

	for dict in dictsList[927*int(length/numero):928*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM927 = np.row_stack((globalFM927,dataArray))
		M += 1
	print(M)

	for dict in dictsList[928*int(length/numero):929*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM928 = np.row_stack((globalFM928,dataArray))
		M += 1
	print(M)

	for dict in dictsList[929*int(length/numero):930*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM929 = np.row_stack((globalFM929,dataArray))
		M += 1
	print(M)

	for dict in dictsList[930*int(length/numero):931*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM930 = np.row_stack((globalFM930,dataArray))
		M += 1
	print(M)

	for dict in dictsList[931*int(length/numero):932*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM931 = np.row_stack((globalFM931,dataArray))
		M += 1
	print(M)

	for dict in dictsList[932*int(length/numero):933*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM932 = np.row_stack((globalFM932,dataArray))
		M += 1
	print(M)

	for dict in dictsList[933*int(length/numero):934*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM933 = np.row_stack((globalFM933,dataArray))
		M += 1
	print(M)

	for dict in dictsList[934*int(length/numero):935*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM934 = np.row_stack((globalFM934,dataArray))
		M += 1
	print(M)

	for dict in dictsList[935*int(length/numero):936*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM935 = np.row_stack((globalFM935,dataArray))
		M += 1
	print(M)

	for dict in dictsList[936*int(length/numero):937*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM936 = np.row_stack((globalFM936,dataArray))
		M += 1
	print(M)

	for dict in dictsList[937*int(length/numero):938*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM937 = np.row_stack((globalFM937,dataArray))
		M += 1
	print(M)

	for dict in dictsList[938*int(length/numero):939*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM938 = np.row_stack((globalFM938,dataArray))
		M += 1
	print(M)

	for dict in dictsList[939*int(length/numero):940*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM939 = np.row_stack((globalFM939,dataArray))
		M += 1
	print(M)

	for dict in dictsList[940*int(length/numero):941*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM940 = np.row_stack((globalFM940,dataArray))
		M += 1
	print(M)

	for dict in dictsList[941*int(length/numero):942*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM941 = np.row_stack((globalFM941,dataArray))
		M += 1
	print(M)

	for dict in dictsList[942*int(length/numero):943*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM942 = np.row_stack((globalFM942,dataArray))
		M += 1
	print(M)

	for dict in dictsList[943*int(length/numero):944*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM943 = np.row_stack((globalFM943,dataArray))
		M += 1
	print(M)

	for dict in dictsList[944*int(length/numero):945*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM944 = np.row_stack((globalFM944,dataArray))
		M += 1
	print(M)

	for dict in dictsList[945*int(length/numero):946*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM945 = np.row_stack((globalFM945,dataArray))
		M += 1
	print(M)

	for dict in dictsList[946*int(length/numero):947*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM946 = np.row_stack((globalFM946,dataArray))
		M += 1
	print(M)

	for dict in dictsList[947*int(length/numero):948*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM947 = np.row_stack((globalFM947,dataArray))
		M += 1
	print(M)

	for dict in dictsList[948*int(length/numero):949*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM948 = np.row_stack((globalFM948,dataArray))
		M += 1
	print(M)

	for dict in dictsList[949*int(length/numero):950*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM949 = np.row_stack((globalFM949,dataArray))
		M += 1
	print(M)

	for dict in dictsList[950*int(length/numero):951*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM950 = np.row_stack((globalFM950,dataArray))
		M += 1
	print(M)

	for dict in dictsList[951*int(length/numero):952*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM951 = np.row_stack((globalFM951,dataArray))
		M += 1
	print(M)

	for dict in dictsList[952*int(length/numero):953*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM952 = np.row_stack((globalFM952,dataArray))
		M += 1
	print(M)

	for dict in dictsList[953*int(length/numero):954*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM953 = np.row_stack((globalFM953,dataArray))
		M += 1
	print(M)

	for dict in dictsList[954*int(length/numero):955*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM954 = np.row_stack((globalFM954,dataArray))
		M += 1
	print(M)

	for dict in dictsList[955*int(length/numero):956*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM955 = np.row_stack((globalFM955,dataArray))
		M += 1
	print(M)

	for dict in dictsList[956*int(length/numero):957*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM956 = np.row_stack((globalFM956,dataArray))
		M += 1
	print(M)

	for dict in dictsList[957*int(length/numero):958*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM957 = np.row_stack((globalFM957,dataArray))
		M += 1
	print(M)

	for dict in dictsList[958*int(length/numero):959*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM958 = np.row_stack((globalFM958,dataArray))
		M += 1
	print(M)

	for dict in dictsList[959*int(length/numero):960*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM959 = np.row_stack((globalFM959,dataArray))
		M += 1
	print(M)

	for dict in dictsList[960*int(length/numero):961*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM960 = np.row_stack((globalFM960,dataArray))
		M += 1
	print(M)

	for dict in dictsList[961*int(length/numero):962*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM961 = np.row_stack((globalFM961,dataArray))
		M += 1
	print(M)

	for dict in dictsList[962*int(length/numero):963*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM962 = np.row_stack((globalFM962,dataArray))
		M += 1
	print(M)

	for dict in dictsList[963*int(length/numero):964*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM963 = np.row_stack((globalFM963,dataArray))
		M += 1
	print(M)

	for dict in dictsList[964*int(length/numero):965*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM964 = np.row_stack((globalFM964,dataArray))
		M += 1
	print(M)

	for dict in dictsList[965*int(length/numero):966*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM965 = np.row_stack((globalFM965,dataArray))
		M += 1
	print(M)

	for dict in dictsList[966*int(length/numero):967*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM966 = np.row_stack((globalFM966,dataArray))
		M += 1
	print(M)

	for dict in dictsList[967*int(length/numero):968*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM967 = np.row_stack((globalFM967,dataArray))
		M += 1
	print(M)

	for dict in dictsList[968*int(length/numero):969*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM968 = np.row_stack((globalFM968,dataArray))
		M += 1
	print(M)

	for dict in dictsList[969*int(length/numero):970*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM969 = np.row_stack((globalFM969,dataArray))
		M += 1
	print(M)

	for dict in dictsList[970*int(length/numero):971*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM970 = np.row_stack((globalFM970,dataArray))
		M += 1
	print(M)

	for dict in dictsList[971*int(length/numero):972*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM971 = np.row_stack((globalFM971,dataArray))
		M += 1
	print(M)

	for dict in dictsList[972*int(length/numero):973*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM972 = np.row_stack((globalFM972,dataArray))
		M += 1
	print(M)

	for dict in dictsList[973*int(length/numero):974*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM973 = np.row_stack((globalFM973,dataArray))
		M += 1
	print(M)

	for dict in dictsList[974*int(length/numero):975*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM974 = np.row_stack((globalFM974,dataArray))
		M += 1
	print(M)

	for dict in dictsList[975*int(length/numero):976*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM975 = np.row_stack((globalFM975,dataArray))
		M += 1
	print(M)

	for dict in dictsList[976*int(length/numero):977*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM976 = np.row_stack((globalFM976,dataArray))
		M += 1
	print(M)

	for dict in dictsList[977*int(length/numero):978*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM977 = np.row_stack((globalFM977,dataArray))
		M += 1
	print(M)

	for dict in dictsList[978*int(length/numero):979*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM978 = np.row_stack((globalFM978,dataArray))
		M += 1
	print(M)

	for dict in dictsList[979*int(length/numero):980*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM979 = np.row_stack((globalFM979,dataArray))
		M += 1
	print(M)

	for dict in dictsList[980*int(length/numero):981*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM980 = np.row_stack((globalFM980,dataArray))
		M += 1
	print(M)

	for dict in dictsList[981*int(length/numero):982*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM981 = np.row_stack((globalFM981,dataArray))
		M += 1
	print(M)

	for dict in dictsList[982*int(length/numero):983*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM982 = np.row_stack((globalFM982,dataArray))
		M += 1
	print(M)

	for dict in dictsList[983*int(length/numero):984*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM983 = np.row_stack((globalFM983,dataArray))
		M += 1
	print(M)

	for dict in dictsList[984*int(length/numero):985*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM984 = np.row_stack((globalFM984,dataArray))
		M += 1
	print(M)

	for dict in dictsList[985*int(length/numero):986*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM985 = np.row_stack((globalFM985,dataArray))
		M += 1
	print(M)

	for dict in dictsList[986*int(length/numero):987*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM986 = np.row_stack((globalFM986,dataArray))
		M += 1
	print(M)

	for dict in dictsList[987*int(length/numero):988*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM987 = np.row_stack((globalFM987,dataArray))
		M += 1
	print(M)

	for dict in dictsList[988*int(length/numero):989*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM988 = np.row_stack((globalFM988,dataArray))
		M += 1
	print(M)

	for dict in dictsList[989*int(length/numero):990*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM989 = np.row_stack((globalFM989,dataArray))
		M += 1
	print(M)

	for dict in dictsList[990*int(length/numero):991*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM990 = np.row_stack((globalFM990,dataArray))
		M += 1
	print(M)

	for dict in dictsList[991*int(length/numero):992*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM991 = np.row_stack((globalFM991,dataArray))
		M += 1
	print(M)

	for dict in dictsList[992*int(length/numero):993*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM992 = np.row_stack((globalFM992,dataArray))
		M += 1
	print(M)

	for dict in dictsList[993*int(length/numero):994*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM993 = np.row_stack((globalFM993,dataArray))
		M += 1
	print(M)

	for dict in dictsList[994*int(length/numero):995*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM994 = np.row_stack((globalFM994,dataArray))
		M += 1
	print(M)

	for dict in dictsList[995*int(length/numero):996*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM995 = np.row_stack((globalFM995,dataArray))
		M += 1
	print(M)

	for dict in dictsList[996*int(length/numero):997*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM996 = np.row_stack((globalFM996,dataArray))
		M += 1
	print(M)

	for dict in dictsList[997*int(length/numero):998*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM997 = np.row_stack((globalFM997,dataArray))
		M += 1
	print(M)

	for dict in dictsList[998*int(length/numero):999*int(length/numero)]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM998 = np.row_stack((globalFM998,dataArray))
		M += 1
	print(M)

	for dict in dictsList[999*int(length/numero):]:
		dataArray = []
		dataArray.append(audioNameList[M])
		dataArray.extend(dict.values())
		globalFM999 = np.row_stack((globalFM999,dataArray))
		M += 1
	print(M)

	globalFMx0 = np.row_stack((globalFM0,globalFM1,globalFM2,globalFM3,globalFM4,globalFM5,globalFM6,globalFM7,globalFM8,globalFM9,globalFM10,globalFM11,globalFM12,globalFM13,globalFM14,globalFM15,globalFM16,globalFM17,globalFM18,globalFM19,globalFM20,globalFM21,globalFM22,globalFM23,globalFM24,globalFM25,globalFM26,globalFM27,globalFM28,globalFM29,globalFM30,globalFM31,globalFM32,globalFM33,globalFM34,globalFM35,globalFM36,globalFM37,globalFM38,globalFM39,globalFM40,globalFM41,globalFM42,globalFM43,globalFM44,globalFM45,globalFM46,globalFM47,globalFM48,globalFM49,globalFM50,globalFM51,globalFM52,globalFM53,globalFM54,globalFM55,globalFM56,globalFM57,globalFM58,globalFM59,globalFM60,globalFM61,globalFM62,globalFM63,globalFM64,globalFM65,globalFM66,globalFM67,globalFM68,globalFM69,globalFM70,globalFM71,globalFM72,globalFM73,globalFM74,globalFM75,globalFM76,globalFM77,globalFM78,globalFM79,globalFM80,globalFM81,globalFM82,globalFM83,globalFM84,globalFM85,globalFM86,globalFM87,globalFM88,globalFM89,globalFM90,globalFM91,globalFM92,globalFM93,globalFM94,globalFM95,globalFM96,globalFM97,globalFM98,globalFM99,))
	globalFMx1 = np.row_stack((globalFM100,globalFM101,globalFM102,globalFM103,globalFM104,globalFM105,globalFM106,globalFM107,globalFM108,globalFM109,globalFM110,globalFM111,globalFM112,globalFM113,globalFM114,globalFM115,globalFM116,globalFM117,globalFM118,globalFM119,globalFM120,globalFM121,globalFM122,globalFM123,globalFM124,globalFM125,globalFM126,globalFM127,globalFM128,globalFM129,globalFM130,globalFM131,globalFM132,globalFM133,globalFM134,globalFM135,globalFM136,globalFM137,globalFM138,globalFM139,globalFM140,globalFM141,globalFM142,globalFM143,globalFM144,globalFM145,globalFM146,globalFM147,globalFM148,globalFM149,globalFM150,globalFM151,globalFM152,globalFM153,globalFM154,globalFM155,globalFM156,globalFM157,globalFM158,globalFM159,globalFM160,globalFM161,globalFM162,globalFM163,globalFM164,globalFM165,globalFM166,globalFM167,globalFM168,globalFM169,globalFM170,globalFM171,globalFM172,globalFM173,globalFM174,globalFM175,globalFM176,globalFM177,globalFM178,globalFM179,globalFM180,globalFM181,globalFM182,globalFM183,globalFM184,globalFM185,globalFM186,globalFM187,globalFM188,globalFM189,globalFM190,globalFM191,globalFM192,globalFM193,globalFM194,globalFM195,globalFM196,globalFM197,globalFM198,globalFM199,))
	globalFMx2 = np.row_stack((globalFM200,globalFM201,globalFM202,globalFM203,globalFM204,globalFM205,globalFM206,globalFM207,globalFM208,globalFM209,globalFM210,globalFM211,globalFM212,globalFM213,globalFM214,globalFM215,globalFM216,globalFM217,globalFM218,globalFM219,globalFM220,globalFM221,globalFM222,globalFM223,globalFM224,globalFM225,globalFM226,globalFM227,globalFM228,globalFM229,globalFM230,globalFM231,globalFM232,globalFM233,globalFM234,globalFM235,globalFM236,globalFM237,globalFM238,globalFM239,globalFM240,globalFM241,globalFM242,globalFM243,globalFM244,globalFM245,globalFM246,globalFM247,globalFM248,globalFM249,globalFM250,globalFM251,globalFM252,globalFM253,globalFM254,globalFM255,globalFM256,globalFM257,globalFM258,globalFM259,globalFM260,globalFM261,globalFM262,globalFM263,globalFM264,globalFM265,globalFM266,globalFM267,globalFM268,globalFM269,globalFM270,globalFM271,globalFM272,globalFM273,globalFM274,globalFM275,globalFM276,globalFM277,globalFM278,globalFM279,globalFM280,globalFM281,globalFM282,globalFM283,globalFM284,globalFM285,globalFM286,globalFM287,globalFM288,globalFM289,globalFM290,globalFM291,globalFM292,globalFM293,globalFM294,globalFM295,globalFM296,globalFM297,globalFM298,globalFM299,))
	globalFMx3 = np.row_stack((globalFM300,globalFM301,globalFM302,globalFM303,globalFM304,globalFM305,globalFM306,globalFM307,globalFM308,globalFM309,globalFM310,globalFM311,globalFM312,globalFM313,globalFM314,globalFM315,globalFM316,globalFM317,globalFM318,globalFM319,globalFM320,globalFM321,globalFM322,globalFM323,globalFM324,globalFM325,globalFM326,globalFM327,globalFM328,globalFM329,globalFM330,globalFM331,globalFM332,globalFM333,globalFM334,globalFM335,globalFM336,globalFM337,globalFM338,globalFM339,globalFM340,globalFM341,globalFM342,globalFM343,globalFM344,globalFM345,globalFM346,globalFM347,globalFM348,globalFM349,globalFM350,globalFM351,globalFM352,globalFM353,globalFM354,globalFM355,globalFM356,globalFM357,globalFM358,globalFM359,globalFM360,globalFM361,globalFM362,globalFM363,globalFM364,globalFM365,globalFM366,globalFM367,globalFM368,globalFM369,globalFM370,globalFM371,globalFM372,globalFM373,globalFM374,globalFM375,globalFM376,globalFM377,globalFM378,globalFM379,globalFM380,globalFM381,globalFM382,globalFM383,globalFM384,globalFM385,globalFM386,globalFM387,globalFM388,globalFM389,globalFM390,globalFM391,globalFM392,globalFM393,globalFM394,globalFM395,globalFM396,globalFM397,globalFM398,globalFM399,))
	globalFMx4 = np.row_stack((globalFM400,globalFM401,globalFM402,globalFM403,globalFM404,globalFM405,globalFM406,globalFM407,globalFM408,globalFM409,globalFM410,globalFM411,globalFM412,globalFM413,globalFM414,globalFM415,globalFM416,globalFM417,globalFM418,globalFM419,globalFM420,globalFM421,globalFM422,globalFM423,globalFM424,globalFM425,globalFM426,globalFM427,globalFM428,globalFM429,globalFM430,globalFM431,globalFM432,globalFM433,globalFM434,globalFM435,globalFM436,globalFM437,globalFM438,globalFM439,globalFM440,globalFM441,globalFM442,globalFM443,globalFM444,globalFM445,globalFM446,globalFM447,globalFM448,globalFM449,globalFM450,globalFM451,globalFM452,globalFM453,globalFM454,globalFM455,globalFM456,globalFM457,globalFM458,globalFM459,globalFM460,globalFM461,globalFM462,globalFM463,globalFM464,globalFM465,globalFM466,globalFM467,globalFM468,globalFM469,globalFM470,globalFM471,globalFM472,globalFM473,globalFM474,globalFM475,globalFM476,globalFM477,globalFM478,globalFM479,globalFM480,globalFM481,globalFM482,globalFM483,globalFM484,globalFM485,globalFM486,globalFM487,globalFM488,globalFM489,globalFM490,globalFM491,globalFM492,globalFM493,globalFM494,globalFM495,globalFM496,globalFM497,globalFM498,globalFM499,))
	globalFMx5 = np.row_stack((globalFM500,globalFM501,globalFM502,globalFM503,globalFM504,globalFM505,globalFM506,globalFM507,globalFM508,globalFM509,globalFM510,globalFM511,globalFM512,globalFM513,globalFM514,globalFM515,globalFM516,globalFM517,globalFM518,globalFM519,globalFM520,globalFM521,globalFM522,globalFM523,globalFM524,globalFM525,globalFM526,globalFM527,globalFM528,globalFM529,globalFM530,globalFM531,globalFM532,globalFM533,globalFM534,globalFM535,globalFM536,globalFM537,globalFM538,globalFM539,globalFM540,globalFM541,globalFM542,globalFM543,globalFM544,globalFM545,globalFM546,globalFM547,globalFM548,globalFM549,globalFM550,globalFM551,globalFM552,globalFM553,globalFM554,globalFM555,globalFM556,globalFM557,globalFM558,globalFM559,globalFM560,globalFM561,globalFM562,globalFM563,globalFM564,globalFM565,globalFM566,globalFM567,globalFM568,globalFM569,globalFM570,globalFM571,globalFM572,globalFM573,globalFM574,globalFM575,globalFM576,globalFM577,globalFM578,globalFM579,globalFM580,globalFM581,globalFM582,globalFM583,globalFM584,globalFM585,globalFM586,globalFM587,globalFM588,globalFM589,globalFM590,globalFM591,globalFM592,globalFM593,globalFM594,globalFM595,globalFM596,globalFM597,globalFM598,globalFM599,))
	globalFMx6 = np.row_stack((globalFM600,globalFM601,globalFM602,globalFM603,globalFM604,globalFM605,globalFM606,globalFM607,globalFM608,globalFM609,globalFM610,globalFM611,globalFM612,globalFM613,globalFM614,globalFM615,globalFM616,globalFM617,globalFM618,globalFM619,globalFM620,globalFM621,globalFM622,globalFM623,globalFM624,globalFM625,globalFM626,globalFM627,globalFM628,globalFM629,globalFM630,globalFM631,globalFM632,globalFM633,globalFM634,globalFM635,globalFM636,globalFM637,globalFM638,globalFM639,globalFM640,globalFM641,globalFM642,globalFM643,globalFM644,globalFM645,globalFM646,globalFM647,globalFM648,globalFM649,globalFM650,globalFM651,globalFM652,globalFM653,globalFM654,globalFM655,globalFM656,globalFM657,globalFM658,globalFM659,globalFM660,globalFM661,globalFM662,globalFM663,globalFM664,globalFM665,globalFM666,globalFM667,globalFM668,globalFM669,globalFM670,globalFM671,globalFM672,globalFM673,globalFM674,globalFM675,globalFM676,globalFM677,globalFM678,globalFM679,globalFM680,globalFM681,globalFM682,globalFM683,globalFM684,globalFM685,globalFM686,globalFM687,globalFM688,globalFM689,globalFM690,globalFM691,globalFM692,globalFM693,globalFM694,globalFM695,globalFM696,globalFM697,globalFM698,globalFM699,))
	globalFMx7 = np.row_stack((globalFM700,globalFM701,globalFM702,globalFM703,globalFM704,globalFM705,globalFM706,globalFM707,globalFM708,globalFM709,globalFM710,globalFM711,globalFM712,globalFM713,globalFM714,globalFM715,globalFM716,globalFM717,globalFM718,globalFM719,globalFM720,globalFM721,globalFM722,globalFM723,globalFM724,globalFM725,globalFM726,globalFM727,globalFM728,globalFM729,globalFM730,globalFM731,globalFM732,globalFM733,globalFM734,globalFM735,globalFM736,globalFM737,globalFM738,globalFM739,globalFM740,globalFM741,globalFM742,globalFM743,globalFM744,globalFM745,globalFM746,globalFM747,globalFM748,globalFM749,globalFM750,globalFM751,globalFM752,globalFM753,globalFM754,globalFM755,globalFM756,globalFM757,globalFM758,globalFM759,globalFM760,globalFM761,globalFM762,globalFM763,globalFM764,globalFM765,globalFM766,globalFM767,globalFM768,globalFM769,globalFM770,globalFM771,globalFM772,globalFM773,globalFM774,globalFM775,globalFM776,globalFM777,globalFM778,globalFM779,globalFM780,globalFM781,globalFM782,globalFM783,globalFM784,globalFM785,globalFM786,globalFM787,globalFM788,globalFM789,globalFM790,globalFM791,globalFM792,globalFM793,globalFM794,globalFM795,globalFM796,globalFM797,globalFM798,globalFM799,))
	globalFMx8 = np.row_stack((globalFM800,globalFM801,globalFM802,globalFM803,globalFM804,globalFM805,globalFM806,globalFM807,globalFM808,globalFM809,globalFM810,globalFM811,globalFM812,globalFM813,globalFM814,globalFM815,globalFM816,globalFM817,globalFM818,globalFM819,globalFM820,globalFM821,globalFM822,globalFM823,globalFM824,globalFM825,globalFM826,globalFM827,globalFM828,globalFM829,globalFM830,globalFM831,globalFM832,globalFM833,globalFM834,globalFM835,globalFM836,globalFM837,globalFM838,globalFM839,globalFM840,globalFM841,globalFM842,globalFM843,globalFM844,globalFM845,globalFM846,globalFM847,globalFM848,globalFM849,globalFM850,globalFM851,globalFM852,globalFM853,globalFM854,globalFM855,globalFM856,globalFM857,globalFM858,globalFM859,globalFM860,globalFM861,globalFM862,globalFM863,globalFM864,globalFM865,globalFM866,globalFM867,globalFM868,globalFM869,globalFM870,globalFM871,globalFM872,globalFM873,globalFM874,globalFM875,globalFM876,globalFM877,globalFM878,globalFM879,globalFM880,globalFM881,globalFM882,globalFM883,globalFM884,globalFM885,globalFM886,globalFM887,globalFM888,globalFM889,globalFM890,globalFM891,globalFM892,globalFM893,globalFM894,globalFM895,globalFM896,globalFM897,globalFM898,globalFM899,))
	globalFMx9 = np.row_stack((globalFM900,globalFM901,globalFM902,globalFM903,globalFM904,globalFM905,globalFM906,globalFM907,globalFM908,globalFM909,globalFM910,globalFM911,globalFM912,globalFM913,globalFM914,globalFM915,globalFM916,globalFM917,globalFM918,globalFM919,globalFM920,globalFM921,globalFM922,globalFM923,globalFM924,globalFM925,globalFM926,globalFM927,globalFM928,globalFM929,globalFM930,globalFM931,globalFM932,globalFM933,globalFM934,globalFM935,globalFM936,globalFM937,globalFM938,globalFM939,globalFM940,globalFM941,globalFM942,globalFM943,globalFM944,globalFM945,globalFM946,globalFM947,globalFM948,globalFM949,globalFM950,globalFM951,globalFM952,globalFM953,globalFM954,globalFM955,globalFM956,globalFM957,globalFM958,globalFM959,globalFM960,globalFM961,globalFM962,globalFM963,globalFM964,globalFM965,globalFM966,globalFM967,globalFM968,globalFM969,globalFM970,globalFM971,globalFM972,globalFM973,globalFM974,globalFM975,globalFM976,globalFM977,globalFM978,globalFM979,globalFM980,globalFM981,globalFM982,globalFM983,globalFM984,globalFM985,globalFM986,globalFM987,globalFM988,globalFM989,globalFM990,globalFM991,globalFM992,globalFM993,globalFM994,globalFM995,globalFM996,globalFM997,globalFM998,globalFM999,))
	globalFM = np.row_stack((globalFMx0,globalFMx1,globalFMx2,globalFMx3,globalFMx4,globalFMx5,globalFMx6,globalFMx7,globalFMx8,globalFMx9,))
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print(f"Features joined!:  {current_time}")
	print("Global fm", globalFM)
	print("M", M)
	print("Number of utterances in global fm",globalFM.shape[0])


	return globalFM